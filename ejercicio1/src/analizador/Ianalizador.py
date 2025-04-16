from html.parser import HTMLParser
from abc import abstractmethod

class IAnalizador(HTMLParser):
    def __init__(self):
        super().__init__()
        self.img_tags = []
        self.current_tag = None
        self.current_attrs = None

    @abstractmethod
    def handle_starttag(self, tag: str, attrs: str)-> None:
        """Captura las etiquetas img y sus atributos."""
