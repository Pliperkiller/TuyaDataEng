from src.orquestador import Orquestador
from src.procesador_imagenes.procesador_imagenes import ProcesadorImagenes
from src.analizador.analizador_html import AnalizadorHTML
from src.buscador_imagenes.buscador_factory import BuscadorFactory
import json
import argparse

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description='Procesa archivos HTML y convierte imágenes a base64')
    parser.add_argument('input', nargs='+', help='Rutas a archivos HTML o directorios que contienen archivos HTML')
    parser.add_argument('--output-json', help='Ruta para guardar resultados en formato JSON')
    
    args = parser.parse_args()
    
    image_processor = ProcesadorImagenes()
    parser = AnalizadorHTML()
    
    buscador_factory = BuscadorFactory()
    
    orquestador = Orquestador(
        image_processor=image_processor,
        parser=parser,
        fetcher_factory=buscador_factory
    )

    results = orquestador.process_files(args.input)
    
    # Mostrar resultados
    success_count = sum(len(files) for files in results["success"].values())
    fail_count = sum(len(files) if isinstance(files, list) else 1 for files in results["fail"].values())
    
    print(f"\nProcesamiento completado:")
    print(f"- Imágenes convertidas exitosamente: {success_count}")
    print(f"- Imágenes que fallaron: {fail_count}")
    
    # Guardar resultados en JSON si se especificó
    if args.output_json:
        with open(args.output_json, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\nResultados guardados en: {args.output_json}")


if __name__ == "__main__":
    main()