from src.buscador.Ibuscador_imagenes import IBuscadorImagenes

class BuscadorLocal(IBuscadorImagenes):
    """Obtiene imágenes del sistema de archivos local."""

    def buscar(self, src: str) -> bytes:
        with open(src, 'rb') as file:
            return file.read()
        
if __name__ == "__main__":
    # Ejemplo de uso
    fetcher = BuscadorLocal()
    image_data = fetcher.buscar(r"D:\Programming\Personal\TechTests\TuyaDataEng\data\raw\images\Capture.PNG")
    print(f"Datos de la imagen: {image_data[:10]}...")  # Muestra los primeros 10 bytes