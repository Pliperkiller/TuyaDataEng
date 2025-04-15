from src.buscador_imagenes.Ibuscador_imagenes import IBuscadorImagenes
#from Ibuscador_imagenes import IBuscadorImagenes
import re
import base64

class BuscadorBase64(IBuscadorImagenes):
    """Obtiene imágenes que ya están en formato base64."""
    
    def leer_imagen(self, src: str) -> bytes:
        pattern = r'data:image/[^;]+;base64,(.+)'
        match = re.match(pattern, src)
        if match:
            return base64.b64decode(match.group(1))
        raise ValueError("Formato de datos URI no válido")

if __name__ == "__main__":
    buscador = BuscadorBase64()
    # Ejemplo de uso
    src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA..."
    try:
        imagen = buscador.leer_imagen(src)
        print("Imagen leída correctamente.")
        print(imagen)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    # Aquí puedes agregar más pruebas o ejemplos de uso
