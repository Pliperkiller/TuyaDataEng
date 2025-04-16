from src.procesador_imagenes.Iprocesador_imagenes import IProcesadorImagenes

class Implementador:
    """
    Clase principal para procesar archivos HTML y convertir sus imágenes a base64.
    Implementa el patrón de diseño Fachada.
    """
    
    def __init__(self):
        self.results = {
            "success": {},
            "fail": {}
        }
        self.image_processor = ImageProcessor()
    
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
        """
        Procesa un archivo HTML específico
        
        Args:
            html_file_path: Ruta al archivo HTML
        """
        with open(html_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Usar nuestro propio parser HTML en lugar de BeautifulSoup
        parser = HTMLParser()
        parser.feed(content)
        
        if not parser.img_tags:
            self.results["success"][html_file_path] = []
            return
        
        base_url = Path(html_file_path).parent.as_uri() + '/'
        processed_images = []
        failed_images = []
        
        # Crear una copia del contenido para modificarlo
        modified_content = content
        
        for _, attrs in parser.img_tags:
            attrs_dict = dict(attrs)
            src = attrs_dict.get('src')
            if not src:
                continue
                
            try:
                # Convertir la URL relativa a absoluta si es necesario
                img_url = self._get_absolute_url(src, base_url, html_file_path)
                
                # Crear el fetcher adecuado según el tipo de URL
                fetcher = FetcherFactory.create_fetcher(img_url)
                
                # Obtener los datos binarios de la imagen
                img_data = fetcher.fetch(img_url)
                
                # Determinar el tipo MIME
                mime_type = self.image_processor.get_mime_type(img_url)
                
                # Convertir a base64
                base64_src = self.image_processor.convert_to_base64(img_data, mime_type)
                
                # Reemplazar la URL original con la versión base64 en el contenido HTML
                # Usamos regex para un reemplazo preciso
                pattern = re.compile(r'(<img[^>]*src\s*=\s*["\'])' + re.escape(src) + r'(["\'][^>]*>)')
                modified_content = pattern.sub(r'\1' + base64_src.replace('\\', '\\\\') + r'\2', modified_content)
                
                processed_images.append(src)
            except Exception as e:
                failed_images.append({"src": src, "error": str(e)})
        
        # Guardar el HTML modificado
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
