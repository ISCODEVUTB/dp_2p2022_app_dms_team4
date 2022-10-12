from abc import ABC, abstractmethod
from typing import List
from enumerations import formats, CategoriaI
class Documentos(ABC):
    __yearn: int
    __authors: List[str]
    __edition: str
    __formats: List[formats]
    __languages: List[str]
    __isbn: str
    __pages: int
    __titles: str
    __Categoria: CategoriaI

    def __init__(self, yearn: int, authors: List[str], edition: str, formats: List[formats], languages: List[str], isbn: str,pages: int, titles: str):
        
        self.__yearn = yearn
        self.__authors = authors
        self.__edition = edition
        self.__formats= formats
        self.__languages= languages
        self.__isbn= isbn
        self.__pages= pages
        self.__titles= titles
        
    
    def Documentos(self):
        pass
    
    def categoria(self, categoria):
        self.__Categoria= categoria
        
    
    def getCategoria(self):
        return self.__Categoria
        
    def __str__(self):
        return  f"nombre: {self.__yearn}, edition: {self.__edition}, titles: {self.__titles},"
    
    
    def __eq__(self, __o: object) -> bool:
        pass
    
    def __hash__(self) -> int:
        return super().__hash__()

