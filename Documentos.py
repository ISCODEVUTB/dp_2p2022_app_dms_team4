from abc import ABC, abstractmethod
from typing import List
from enumerations import Formatos
class Documentos(ABC):
    __Anno: int
    __Autores: List[str]
    __Edicion: str
    __Formatos: List[Formatos]
    __Idiomas: List[str]
    __isbn: str
    __paginas: int
    __titulo: str


    def __init__(self, **kwargs):
        self.__Anno = kwargs['Anno']
        self.__Autores = kwargs['Autores']
        self.__Edicion = kwargs['Edicion']
        self.__Formatos= kwargs['Formatos']
        self.__Idiomas= kwargs['Idiomas']
        self.__isbn= kwargs['Isbn']
        self.__paginas= kwargs['Paginas']
        self.__titulo= kwargs['titulo']
        
    def Documentos(self):
        pass
    @abstractmethod
    def categoria(self)->str:
        pass


