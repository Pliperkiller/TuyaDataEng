from src.procesador_imagenes.Iprocesador_imagenes import IProcesadorImagenes
import mimetypes
import re
import os
import base64

class ProcesadorImagenes(IProcesadorImagenes):
    def __init__(self):
        # Asegurar que mimetypes esté inicializado
        if not mimetypes.inited:
            mimetypes.init()

    def obtener_formato_imagen(self, url):
        if url.startswith('data:'):
            pattern = r'data:(image/[^;]+);'
            match = re.match(pattern, url)
            if match:
                return match.group(1)
            return "image/jpeg"
        
        extension = os.path.splitext(url)[1].lower()
        mime_type = mimetypes.guess_type(url)[0]
        
        if not mime_type or not mime_type.startswith('image/'):
            # Extensiones comunes como respaldo
            mime_map = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.svg': 'image/svg+xml',
                '.webp': 'image/webp',
                '.bmp': 'image/bmp',
                '.ico': 'image/x-icon'
            }
            mime_type = mime_map.get(extension, 'image/jpeg')
        
        return mime_type
    
    def convertir_base64(self, imagen_bin, formato):
        base64_data = base64.b64encode(imagen_bin).decode('utf-8')
        return f"data:{formato};base64,{base64_data}"

if __name__ == "__main__":
    procesador = ProcesadorImagenes()
