from src.buscador_imagenes.Ibuscador_imagenes import IBuscadorImagenes
#from Ibuscador_imagenes import IBuscadorImagenes

from urllib.request import urlopen


class RemoteImageFetcher(IBuscadorImagenes):
    """Obtiene imágenes de URLs remotas."""
    
    def leet_imagen(self, src: str) -> bytes:
        with urlopen(src, timeout=10) as response:
            return response.read()
        
if __name__ == "__main__":
    # Ejemplo de uso
    fetcher = RemoteImageFetcher()
    image_data = fetcher.leet_imagen("https://cdn.outsideonline.com/wp-content/uploads/2023/03/Funny_Dog_S.jpg")
    print(f"Datos de la imagen: {image_data[:10]}...")  # Muestra los primeros 10 bytes