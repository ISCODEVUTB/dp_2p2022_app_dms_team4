from DocumentAbstracbFactory import DocumentAbstracbFactory
from Libro import Libro

class LibroFactory(DocumentAbstracbFactory):

    def crearDocumento(self, **kwargs):
        return Libro(**kwargs)