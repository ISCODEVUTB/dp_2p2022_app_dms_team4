from typing import List
from Documentos import Documentos
from IOnline import IOnline
from enumerations import formats, CategoriaI

class Revista(Documentos, IOnline):

    def __init__(self, yearn: int, authors: List[str], edition: str, formats: List[formats], languages: List[str], isbn: str,pages: int, titles: str):
        super().__init__(yearn, authors, edition, formats, languages, isbn,pages,titles)

    def itemOnline(self) -> str:
        return "Soy una Revista Online"
    