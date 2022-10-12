from Documentos import Documentos
from IPdf import IPdf
from enumerations import formats, CategoriaI
from typing import List
class Libro(Documentos, IPdf):

    def __init__(self, yearn: int, authors: List[str], edition: str, formats: List[formats], languages: List[str], isbn: str,pages: int, titles: str):
        super().__init__(yearn, authors, edition, formats, languages, isbn,pages,titles)

    def operaciones(self):
        return "Haciendo Operaciones!"

   

