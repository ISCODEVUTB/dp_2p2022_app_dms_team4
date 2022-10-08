from DocumentAbstracbFactory import DocumentAbstracbFactory
from Cientifico import Cientifico

class CientificoFactory(DocumentAbstracbFactory):

    def crearDocumento(self, Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo):
        return Cientifico(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)