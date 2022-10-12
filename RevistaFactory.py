from DocumentAbstracbFactory import DocumentAbstracbFactory
from Revista import Revista

class RevistaFactory(DocumentAbstracbFactory):

    def __init__(self):
        pass
    def crearDocumento(self,yearn, authors, edition, formats, languages, isbn,pages,titles):
        return Revista(yearn, authors, edition, formats, languages, isbn,pages,titles)