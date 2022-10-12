from enum import Enum


class formats(Enum):
    IMPRESO = 'IMPRESO'
    DIGITAL = "DIGITAL"
    AUDIO = "AUDIO"

class CategoriaI(Enum):
    ARTE= "ARTE"
    DERECHO_CIVIL = "DERECHO_CIVIL"
    INGENIERIA = "INGENIERIA"