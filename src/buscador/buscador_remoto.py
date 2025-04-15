from src.buscador.Ibuscador_imagenes import IBuscadorImagenes
from urllib.request import urlopen


class RemoteImageFetcher(IBuscadorImagenes):
    """Obtiene imágenes de URLs remotas."""
    
    def fetch(self, src: str) -> bytes:
        with urlopen(src, timeout=10) as response:
            return response.read()