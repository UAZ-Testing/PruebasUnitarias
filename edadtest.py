# coding=utf-8

import unittest
from edad import Edad


class EdadTest(unittest.TestCase):
    # Test fixtures

    def setUp(self):
        self.edad = Edad()

    def tearDown(self):
        pass

    # Prueba del valor de inicio

    def test_datos_invalidos(self):
        self.assertEqual(self.edad.evaluar_edad('a'),
                         'debes insertar un número')

    def test_recien_nacido(self):
        self.assertEqual(self.edad.evaluar_edad(0), 'eres un recién nacido')

    def test_inexistente(self):
        self.assertEqual(self.edad.evaluar_edad(-1), 'no existes')

    def test_nino(self):
        self.assertEqual(self.edad.evaluar_edad(12), 'eres niño')

    def test_adolescente(self):
        self.assertEqual(self.edad.evaluar_edad(17), 'eres adolescente')

    def test_adulto(self):
            self.assertEqual(self.edad.evaluar_edad(64), 'eres adulto')

    def test_adulto_mayor(self):
            self.assertEqual(self.edad.evaluar_edad(119), 'eres adulto mayor')

    def test_mumm_ra_1(self):
            self.assertEqual(self.edad.evaluar_edad(120), 'eres Mumm-Ra')

    def test_mumm_ra_2(self):
            self.assertEqual(self.edad.evaluar_edad(121), 'eres Mumm-Ra')


# Ejecuta las pruebas implementadas

if __name__ == '__main__':
    unittest.main()
