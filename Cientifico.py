from Documentos import Documentos
from IOnline import IOnline
from IPdf import IPdf

class Cientifico(Documentos, IOnline, IPdf):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def operaciones(self) -> str:
        return "Haciendo operaciones cientificas!"

    def itemOnline(self) ->str:
        return "Documento Cientifico Online"