from DocumentAbstracbFactory import DocumentAbstracbFactory
from enumerations import *
from RevistaFactory import RevistaFactory
def Cliente(factory: DocumentAbstracbFactory):

    factory_product = factory.crearDocumento(2001,["Juan Perez"],"LAPORTE",formats.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")

    return factory_product

datos_1 = {'yearn': 2001,
"authors": ['Juan Daniel','Gian Valdiris'],
"edition": "LAPORTE","languages":["Español"],
"isbn":"NOSE",
"pages": 500,
"titles":"Cincuenta algoritmos profesionales", 
"formats": [formats.AUDIO, formats.DIGITAL]}

