from Documentos import Documentos
from IPdf import IPdf
from enumerations import Formatos, CategoriaI
from typing import List
class Libro(Documentos, IPdf):

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, Formatos: List[Formatos], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        super().__init__(Anno, Autores, Edicion, Formatos, Idiomas, Isbn,Paginas,Titulo)

    def operaciones(self):
        return "Haciendo Operaciones!"

   

