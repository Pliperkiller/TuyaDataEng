from abc import ABC, abstractmethod

class IAnalizador(ABC):
    @abstractmethod
    def handle_starttag(self, tag: str, attrs: str)-> None:
        """Captura las etiquetas img y sus atributos."""
