from src.buscador_imagenes.buscadores_impl.buscador_base64 import BuscadorBase64
from src.buscador_imagenes.buscadores_impl.buscador_local import BuscadorLocal
from src.buscador_imagenes.buscadores_impl.buscador_remoto import BuscadorURL
from src.buscador_imagenes.Ibuscador_imagenes import IBuscadorImagenes

class BuscadorFactory:
    """Fábrica para crear el fetcher adecuado según el tipo de fuente."""
    
    @staticmethod
    def crear_buscador(src: str) -> IBuscadorImagenes:
        if src.startswith('data:'):
            return BuscadorBase64()
        elif src.startswith(('http://', 'https://')):
            return BuscadorURL()
        else:
            return BuscadorLocal()
        
if __name__ == '__main__':
    buscador = BuscadorFactory.crear_buscador('https://example.com/image.jpg')
    print(type(buscador))  # Debe imprimir <class 'src.buscador_imagenes.buscadores_impl.buscador_remoto.BuscadorURL'>