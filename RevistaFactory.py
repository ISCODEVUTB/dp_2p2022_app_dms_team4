from DocumentAbstracbFactory import DocumentAbstracbFactory
from Revista import Revista

class RevistaFactory(DocumentAbstracbFactory):

    def crearDocumento(self, **kwargs):
        return Revista(**kwargs)