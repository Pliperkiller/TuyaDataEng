from abc import ABC, abstractmethod

class IProcesadorImagenes(ABC):
    """Procesa imágenes y las convierte a formato base64."""
    
    @abstractmethod
    def obtener_formato_imagen(self, url: str) -> str:
        """Determina el tipo MIME de una imagen basado en su extensión.
        
        Args:
            url: URL o ruta de la imagen
            
        Returns:
            str: Tipo MIME
        """
        pass

    @abstractmethod
    def convertir_base64(self, imagen_bin: bytes, formato: str) -> str:
        """Convierte datos binarios a una cadena base64.
        
        Args:
            imagen_bin: Datos binarios de la imagen
            formato: Tipo MIME de la imagen
            
        Returns:
            str: Cadena base64 con prefijo data URI
        """
        pass