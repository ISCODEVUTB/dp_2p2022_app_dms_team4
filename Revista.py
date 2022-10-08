from typing import List
from Documentos import Documentos
from IOnline import IOnline
from enumerations import Formatos, CategoriaI

class Revista(Documentos, IOnline):

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, Formatos: List[Formatos], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        super().__init__(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)

    def itemOnline(self) -> str:
        return "Soy una Revista Online"
    