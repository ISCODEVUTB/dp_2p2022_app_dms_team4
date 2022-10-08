from DocumentAbstracbFactory import DocumentAbstracbFactory
from enumerations import *
from RevistaFactory import RevistaFactory
def Cliente(factory: DocumentAbstracbFactory):

    factory_product = factory.crearDocumento(2001,["Juan Perez"],"LAPORTE",Formatos.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")

    return factory_product

datos_1 = {'Anno': 2001,
"Autores": ['Juan Daniel','Gian Valdiris'],
"Edicion": "LAPORTE","Idiomas":["Español"],
"Isbn":"NOSE",
"Paginas": 500,
"Titulo":"Cincuenta algoritmos profesionales", 
"Formatos": [Formatos.AUDIO, Formatos.DIGITAL]}

