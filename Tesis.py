from typing import List
from Documentos import Documentos
from enumerations import CategoriaI
from enumerations import Formatos


class Tesis(Documentos):

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, Formatos: List[Formatos], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        super().__init__(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)

    