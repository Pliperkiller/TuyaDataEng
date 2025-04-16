from src.procesador_imagenes.Iprocesador_imagenes import IProcesadorImagenes
from src.buscador_imagenes.Ibuscador_imagenes import IBuscadorImagenes
from src.analizador.Ianalizador import IAnalizador
from src.buscador_imagenes.buscador_factory import BuscadorFactory 
from typing import Dict, List, Set, Tuple, Union
from pathlib import Path
import urllib.parse
import re
import os

class Orquestador:
    """
    Clase principal para procesar archivos HTML y convertir sus imágenes a base64.
    """
    
    def __init__(self, 
                image_processor: IProcesadorImagenes = None,
                parser: IAnalizador = None,
                fetcher_factory: BuscadorFactory = None,
                 ):
        self.image_processor = image_processor
        self.fetcher_factory = fetcher_factory or BuscadorFactory()
        self.parser = parser

        self.results = {
            "success": {},
            "fail": {}
        }
    
    def process_files(self, input_paths: Union[List[str], str]) -> Dict:
        """
        Procesa uno o varios archivos HTML o directorios
        
        Args:
            input_paths: Ruta o lista de rutas a archivos o directorios
            
        Returns:
            Dict: Diccionario con resultados de procesamiento
        """
        if isinstance(input_paths, str):
            input_paths = [input_paths]
            
        html_files = self._collect_html_files(input_paths)
        
        for html_file in html_files:
            try:
                self._process_html_file(html_file)
            except Exception as e:
                self.results["fail"][html_file] = str(e)
                
        return self.results
                
    def _collect_html_files(self, paths: List[str]) -> List[str]:
        """
        Recopila todos los archivos HTML de las rutas proporcionadas
        
        Args:
            paths: Lista de rutas a archivos o directorios
            
        Returns:
            List[str]: Lista de rutas completas a archivos HTML
        """
        html_files = []
        
        for path in paths:
            path_obj = Path(path)
            
            if path_obj.is_file() and path_obj.suffix.lower() in ['.html', '.htm']:
                html_files.append(str(path_obj))
            elif path_obj.is_dir():
                # Buscar recursivamente todos los archivos HTML en el directorio
                for html_file in path_obj.glob('**/*.html'):
                    html_files.append(str(html_file))
                for html_file in path_obj.glob('**/*.htm'):
                    html_files.append(str(html_file))
                    
        return html_files
    
    def _process_html_file(self, html_file_path: str) -> None:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        parser = self.parser
        parser.feed(content)
        
        if not parser.img_tags:
            self.results["success"][html_file_path] = []
            return
        
        # Convertir la ruta a absoluta antes de usar as_uri
        base_url = Path(html_file_path).resolve().parent.as_uri() + '/'
        processed_images = []
        failed_images = []
        
        modified_content = content
        
        for _, attrs in parser.img_tags:
            attrs_dict = dict(attrs)
            src = attrs_dict.get('src')
            if not src:
                continue
                
            try:
                img_url = self._get_absolute_url(src, base_url, html_file_path)
                fetcher: IBuscadorImagenes = self.fetcher_factory.crear_buscador(img_url)
                img_data = fetcher.leer_imagen(img_url)
                mime_type = self.image_processor.obtener_formato_imagen(img_url)
                base64_src = self.image_processor.convertir_base64(img_data, mime_type)
                pattern = re.compile(r'(<img[^>]*src\s*=\s*["\'])' + re.escape(src) + r'(["\'][^>]*>)')
                modified_content = pattern.sub(r'\1' + base64_src.replace('\\', '\\\\') + r'\2', modified_content)
                processed_images.append(src)
            except Exception as e:
                failed_images.append({"src": src, "error": str(e)})
        
        output_path = self._get_output_path(html_file_path)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        if processed_images:
            self.results["success"][html_file_path] = processed_images
        if failed_images:
            self.results["fail"][html_file_path] = failed_images
    
    def _get_absolute_url(self, url: str, base_url: str, html_file_path: str) -> str:
        """
        Convierte una URL relativa en absoluta
        
        Args:
            url: URL de la imagen (puede ser relativa)
            base_url: URL base del archivo HTML
            html_file_path: Ruta al archivo HTML
            
        Returns:
            str: URL absoluta o ruta local absoluta
        """
        if url.startswith(('http://', 'https://', 'data:')):
            return url
            
        # Si es una ruta relativa al sistema de archivos
        try:
            if url.startswith('/'):
                # Ruta absoluta desde la raíz
                return url
            else:
                # Ruta relativa al archivo HTML
                html_dir = os.path.dirname(os.path.abspath(html_file_path))
                return os.path.normpath(os.path.join(html_dir, url))
        except Exception:
            # Si falla, intentamos con URL
            return urllib.parse.urljoin(base_url, url)
    
    def _get_output_path(self, input_path: str) -> str:
        """
        Genera la ruta para el archivo HTML procesado
        
        Args:
            input_path: Ruta del archivo HTML original
            
        Returns:
            str: Ruta para el archivo procesado
        """
        path_obj = Path(input_path)
        directory = path_obj.parent
        filename = path_obj.stem + "_base64" + path_obj.suffix
        return str(directory / filename)

if __name__ == "__main__":
    # Ejemplo de uso
    from src.procesador_imagenes.procesador_imagenes import ProcesadorImagenes
    from src.analizador.analizador_html import AnalizadorHTML

    
    image_processor = ProcesadorImagenes()
    parser = AnalizadorHTML()
    
    # Crear el factory con las implementaciones necesarias
    buscador_factory = BuscadorFactory()
    
    orquestador = Orquestador(
        image_processor=image_processor,
        parser=parser,
        fetcher_factory=buscador_factory
    )
    
    results = orquestador.process_files(["ejemplo.html"])
    
    print("Resultados del procesamiento:")
    print(results)