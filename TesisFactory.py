from DocumentAbstracbFactory import DocumentAbstracbFactory
from Tesis import Tesis

class TesisFactory(DocumentAbstracbFactory):

    def crearDocumento(self, yearn, authors, edition, formats, languages, isbn,pages,titles):
        return Tesis(yearn, authors, edition, formats, languages, isbn,pages,titles)