# coding=utf-8

import unittest
from calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_igual_a_cero(self):
        self.assertEqual(self.calc.get_resultado(), 0)

    def test_suma_2_mas_2_igual_4(self):
        self.calc.suma(2, 2)
        self.assertEqual(self.calc.get_resultado(), 4)

    def test_suma_3_mas_3_igual_6(self):
        self.calc.suma(3, 3)
        self.assertEqual(self.calc.get_resultado(), 6)

    def test_suma_menos_1_mas_2_igual_1(self):
        self.calc.suma(-1, 2)
        self.assertEqual(self.calc.get_resultado(), 1)

    def test_suma_L_mas_2_datos_invalidos(self):
        self.calc.suma('L', 2)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

if __name__ == '__main__':
    unittest.main()
