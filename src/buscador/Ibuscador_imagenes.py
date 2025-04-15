from abc import ABC, abstractmethod
class IBuscadorImagenes(ABC):
    """Interfaz para obtener datos de imágenes de diferentes fuentes."""
    
    @abstractmethod
    def buscar(self, src: str) -> bytes:
        """Obtiene los datos binarios de la imagen.
        
        Args:
            src: URL o ruta de la imagen
            
        Returns:
            bytes: Datos binarios de la imagen
        """
        pass