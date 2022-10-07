from Documentos import Documentos
from IPdf import IPdf

class Libro(Documentos, IPdf):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def operaciones(self):
        return "Haciendo Operaciones!"

