import unittest 

from enumerations import *
from RevistaFactory import RevistaFactory
from LibroFactory import LibroFactory
from CientificoFactory import CientificoFactory
from TesisFactory import TesisFactory
from Libro import Libro 
from Revista import Revista
from Cientifico import Cientifico
from Tesis import Tesis

from cliente import Cliente

class testFactories(unittest.TestCase):

    def test_revista_factory(self):
        revista1 = Cliente(RevistaFactory())
        self.assertEqual(revista1.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(revista1, Revista))
    def test_tesis_factory(self):
        tesis = Cliente(TesisFactory())
        self.assertEqual(tesis.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(tesis, Tesis))
    def test_cientifico_factory(self):
        cientf = Cliente(CientificoFactory())
        self.assertEqual(cientf.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(cientf, Cientifico))
    def test_libro_factory(self):
        libro = Cliente(LibroFactory())
        self.assertEqual(libro.__str__(), "nombre: 2001, edicion: LAPORTE, titulo: Fundamento Algoritmo,")
        self.assertTrue(isinstance(libro, Libro))
if __name__ == "__main__":
    unittest.main()