from src.buscador_imagenes.Ibuscador_imagenes import IBuscadorImagenes
#Ibuscador_imagenes import IBuscadorImagenes

class BuscadorLocal(IBuscadorImagenes):
    """Obtiene imágenes del sistema de archivos local."""

    def leer_imagen(self, src: str) -> bytes:
        with open(src, 'rb') as file:
            return file.read()
        
if __name__ == "__main__":
    # Ejemplo de uso
    fetcher = BuscadorLocal()
    image_data = fetcher.leer_imagen(r"D:\Programming\Personal\TechTests\TuyaDataEng\data\raw\images\Capture.PNG")
    print(f"Datos de la imagen: {image_data[:10]}...")  # Muestra los primeros 10 bytes