from DocumentAbstracbFactory import DocumentAbstracbFactory
from Libro import Libro

class LibroFactory(DocumentAbstracbFactory):

    def crearDocumento(self, Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo):
        return Libro(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)