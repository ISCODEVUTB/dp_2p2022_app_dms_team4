from enum import Enum


class Formatos(Enum):
    IMPRESO = 'IMPRESO'
    DIGITAL = "DIGITAL"
    AUDIO = "AUDIO"

class CategoriaI(Enum):
    ARTE= "ARTE"
    DERECHO_CIVIL = "DERECHO_CIVIL"
    INGENIERIA = "INGENIERIA"