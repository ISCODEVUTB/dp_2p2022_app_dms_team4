from abc import ABC , abstractmethod
from Documentos import Documentos

class DocumentAbstracbFactory(ABC):

    @abstractmethod
    def crearDocumento(self):
        pass

    