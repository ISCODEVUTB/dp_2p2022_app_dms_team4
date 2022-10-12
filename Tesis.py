from typing import List
from Documentos import Documentos
from enumerations import CategoriaI
from enumerations import formats


class Tesis(Documentos):

    def __init__(self, yearn: int, authors: List[str], edition: str, formats: List[formats], languages: List[str], isbn: str,pages: int, titles: str):
        super().__init__(yearn, authors, edition, formats, languages, isbn,pages,titles)

    