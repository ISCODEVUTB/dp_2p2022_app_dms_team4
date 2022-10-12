from Documentos import Documentos
from IOnline import IOnline
from IPdf import IPdf
from enumerations import formats, CategoriaI
from typing import List
class Cientifico(Documentos, IOnline, IPdf):

    def __init__(self, yearn: int, authors: List[str], edition: str, formats: List[formats], languages: List[str], isbn: str,pages: int, titles: str):
        super().__init__(yearn, authors, edition, formats, languages, isbn,pages,titles)

    def operaciones(self) -> str:
        return "Haciendo operaciones cientificas!"

    def itemOnline(self) ->str:
        return "Documento Cientifico Online"
    
    