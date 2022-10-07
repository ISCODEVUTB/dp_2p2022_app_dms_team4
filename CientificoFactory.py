from DocumentAbstracbFactory import DocumentAbstracbFactory
from Cientifico import Cientifico

class CientificoFactory(DocumentAbstracbFactory):

    def crearDocumento(self, **kwargs):
        return Cientifico(**kwargs)