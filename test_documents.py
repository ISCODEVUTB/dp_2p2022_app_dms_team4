import unittest 

from enumerations import *
from Documentos import Documentos
from Libro import Libro 
from Revista import Revista
from Cientifico import Cientifico
from Tesis import Tesis


class TestDocumentos(unittest.TestCase):
    datos_1 = {'yearn': 2001,
"authors": ['Juan Daniel','Gian Valdiris'],
"edition": "LAPORTE","languages":["Español"],
"isbn":"NOSE",
"pages": 500,
"titles":"Cincuenta algoritmos profesionales", 
"formats": [formats.AUDIO, formats.DIGITAL]}
    
    #Revista1 = Revista(**datos_1)
    #Tesis1 = Tesis(datos_1)
    #Cientifico1 = Cientifico(datos_1)
    def test_libro(self):
        libro1 = Libro(2001,["Juan Perez"],"LAPORTE",formats.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(libro1.__str__(), "nombre: 2001, edition: LAPORTE, titles: Fundamento Algoritmo,")

    def test_revista(self):
        revista1 = Revista(2001,["Juan Perez"],"LAPORTE",formats.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(revista1.__str__(), "nombre: 2001, edition: LAPORTE, titles: Fundamento Algoritmo,")
    def test_tesis(self):
        tesis = Tesis(2001,["Juan Perez"],"LAPORTE",formats.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(tesis.__str__(), "nombre: 2001, edition: LAPORTE, titles: Fundamento Algoritmo,")
    def test_cientifico(self):
        cientf = Cientifico(2001,["Juan Perez"],"LAPORTE",formats.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(cientf.__str__(), "nombre: 2001, edition: LAPORTE, titles: Fundamento Algoritmo,")
    def test_setCategory(self):
        libro1 = Libro(2001,["Juan Perez"],"LAPORTE",formats.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        libro1.categoria(CategoriaI.INGENIERIA)
        self.assertEqual(libro1.getCategoria(), CategoriaI.INGENIERIA)
if __name__ == "__main__":
    unittest.main()