# coding=utf-8

import unittest
from calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_igual_a_cero(self):
        self.assertEqual(self.calc.get_resultado(), 0)

    def test_sumar_2_mas_2_igual_4(self):
        self.calc.suma(2, 2)
        self.assertEqual(self.calc.get_resultado(), 4)

if __name__ == '__main__':
    unittest.main()
