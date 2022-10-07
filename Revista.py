from Documentos import Documentos
from IOnline import IOnline

class Revista(Documentos, IOnline):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def itemOnline(self) -> str:
        return "Soy una Revista Online"