from abc import ABC, abstractmethod

class Analizador(ABC):
    """Parser HTML personalizado para encontrar etiquetas img."""
    
    def __init__(self):
        super().__init__()
        self.img_tags = []
        self.current_tag = None
        self.current_attrs = None
    
    def capturar_etiquetas(self, tag, attrs):
        """Captura las etiquetas img y sus atributos."""
        if tag == "img":
            attrs_dict = dict(attrs)
            if "src" in attrs_dict:
                self.img_tags.append((tag, attrs))