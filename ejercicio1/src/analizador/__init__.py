from html.parser import HTMLParser

class AnalizadorHTML(HTMLParser):
    """Parser HTML personalizado para encontrar etiquetas img."""
    
    def __init__(self):
        super().__init__()
        self.img_tags = []
        self.current_tag = None
        self.current_attrs = None
    
    def handle_starttag(self, tag, attrs):
        """Captura las etiquetas img y sus atributos."""
        if tag == "img":
            attrs_dict = dict(attrs)
            if "src" in attrs_dict:
                self.img_tags.append((tag, attrs))


if __name__ == "__main__":
    # Ejemplo de uso
    html_content = """
    <html>
        <body>
            <img src="image1.jpg" alt="Image 1">
            <img src="image2.png" alt="Image 2">
        </body>
    </html>
    """

    parser = AnalizadorHTML()
    parser.feed(html_content)
    
    for tag, attrs in parser.img_tags:
        print(f"Etiqueta: {tag}, Atributos: {attrs}")