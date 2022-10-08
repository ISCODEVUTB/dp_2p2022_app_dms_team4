from DocumentAbstracbFactory import DocumentAbstracbFactory
from Tesis import Tesis

class TesisFactory(DocumentAbstracbFactory):

    def crearDocumento(self, Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo):
        return Tesis(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)