from abc import ABC, abstractmethod
from typing import List
from enumerations import Formatos, CategoriaI
class Documentos(ABC):
    __Anno: int
    __Autores: List[str]
    __Edicion: str
    __Formatos: List[Formatos]
    __Idiomas: List[str]
    __isbn: str
    __paginas: int
    __titulo: str
    __Categoria: CategoriaI

    def __init__(self, Anno: int, Autores: List[str], Edicion: str, Formatos: List[Formatos], Idiomas: List[str], Isbn: str,Paginas: int, Titulo: str):
        
        self.__Anno = Anno
        self.__Autores = Autores
        self.__Edicion = Edicion
        self.__Formatos= Formatos
        self.__Idiomas= Idiomas
        self.__isbn= Isbn
        self.__paginas= Paginas
        self.__titulo= Titulo
        
    
    def Documentos(self):
        pass
    
    def categoria(self, categoria):
        self.__Categoria= categoria
        
    
    def getCategoria(self):
        return self.__Categoria
        
    def __str__(self):
        return  f"nombre: {self.__Anno}, edicion: {self.__Edicion}, titulo: {self.__titulo},"
    
    
    def __eq__(self, __o: object) -> bool:
        pass
    
    def __hash__(self) -> int:
        return super().__hash__()

