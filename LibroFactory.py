from DocumentAbstracbFactory import DocumentAbstracbFactory
from Libro import Libro

class LibroFactory(DocumentAbstracbFactory):

    def crearDocumento(self, yearn, authors, edition, formats, languages, isbn,pages,titles):
        return Libro(yearn, authors, edition, formats, languages, isbn,pages,titles)