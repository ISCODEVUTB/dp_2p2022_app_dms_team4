import unittest 

from enumerations import *
from Documentos import Documentos
from Libro import Libro 
from Revista import Revista
from Cientifico import Cientifico
from Tesis import Tesis


class TestDocumentos(unittest.TestCase):
    datos_1 = {'Anno': 2001,
"Autores": ['Juan Daniel','Gian Valdiris'],
"Edicion": "LAPORTE","Idiomas":["Español"],
"Isbn":"NOSE",
"Paginas": 500,
"Titulo":"Cincuenta algoritmos profesionales", 
"Formatos": [Formatos.AUDIO, Formatos.DIGITAL]}
    
    #Revista1 = Revista(**datos_1)
    #Tesis1 = Tesis(datos_1)
    #Cientifico1 = Cientifico(datos_1)
    def test_libro(self):
        libro1 = Libro(2001,["Juan Perez"],"LAPORTE",Formatos.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(libro1.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")

    def test_revista(self):
        revista1 = Revista(2001,["Juan Perez"],"LAPORTE",Formatos.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(revista1.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
    def test_tesis(self):
        tesis = Tesis(2001,["Juan Perez"],"LAPORTE",Formatos.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(tesis.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
    def test_cientifico(self):
        cientf = Cientifico(2001,["Juan Perez"],"LAPORTE",Formatos.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        self.assertEqual(cientf.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
    def test_setCategory(self):
        libro1 = Libro(2001,["Juan Perez"],"LAPORTE",Formatos.DIGITAL,["Español"],"NOSE",192,"Fundamento Algoritmo")
        libro1.categoria(CategoriaI.INGENIERIA)
        self.assertEqual(libro1.getCategoria(), CategoriaI.INGENIERIA)
if __name__ == "__main__":
    unittest.main()