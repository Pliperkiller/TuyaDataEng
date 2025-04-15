from html.parser import HTMLParser
from src.analizador.Ianalizador import IAnalizador
#from Ianalizador import IAnalizador

class AnalizadorHTML(IAnalizador,HTMLParser):
    """Se encarga de identificar las etiquetas HTML que poseen las fuentes de las imágenes"""
    
    def __init__(self):
        super().__init__()
        self.img_tags = []
        self.current_tag = None
        self.current_attrs = None
    
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attrs_dict = dict(attrs)
            if "src" in attrs_dict:
                self.img_tags.append((tag, attrs))

if __name__ == "__main__":
    # Ejemplo de uso
    html_content =( 
    """
<html>
<body>
    <img src="imagen1.jpg" alt="Primera imagen">
    <p>Texto de ejemplo</p>
    <img src="imagen2.png" width="300">
    <div>Otro texto</div>
    <span><img></span>  <!-- Esta no cuenta porque no tiene src -->
</body>
</html>
    """
    )

    parser = AnalizadorHTML()
    parser.feed(html_content)
    
    print(parser.img_tags)
    print(len(parser.img_tags))