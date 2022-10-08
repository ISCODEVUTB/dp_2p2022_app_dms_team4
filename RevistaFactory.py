from DocumentAbstracbFactory import DocumentAbstracbFactory
from Revista import Revista

class RevistaFactory(DocumentAbstracbFactory):

    def __init__(self):
        pass
    def crearDocumento(self,Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo):
        return Revista(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)