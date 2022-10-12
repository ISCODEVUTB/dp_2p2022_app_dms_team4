from DocumentAbstracbFactory import DocumentAbstracbFactory
from Cientifico import Cientifico

class CientificoFactory(DocumentAbstracbFactory):

    def crearDocumento(self, yearn, authors, edition, formats, languages, isbn,pages,titles):
        return Cientifico(yearn, authors, edition, formats, languages, isbn,pages,titles)