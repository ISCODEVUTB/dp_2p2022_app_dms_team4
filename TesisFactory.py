from DocumentAbstracbFactory import DocumentAbstracbFactory
from Tesis import Tesis

class TesisFactory(DocumentAbstracbFactory):

    def crearDocumento(self, **kwargs):
        return Tesis(**kwargs)