# coding=utf-8

import unittest
from calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):
    # Test fixtures

    def setUp(self):
        self.calc = Calculadora()

    def tearDown(self):
        pass

    # Prueba del valor de inicio

    def test_valor_de_inicio_igual_a_cero(self):
        self.assertEqual(self.calc.get_resultado(), 0)

    # Pruebas del método sumar

    def test_suma_2_mas_2_igual_4(self):
        self.calc.sumar(2, 2)
        self.assertEqual(self.calc.get_resultado(), 4)

    def test_suma_3_mas_3_igual_6(self):
        self.calc.sumar(3, 3)
        self.assertEqual(self.calc.get_resultado(), 6)

    def test_suma_menos_1_mas_2_igual_1(self):
        self.calc.sumar(-1, 2)
        self.assertEqual(self.calc.get_resultado(), 1)

    def test_suma_L_mas_2_datos_invalidos(self):
        self.calc.sumar('L', 2)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método restar

    def test_resta_2_menos_2_igual_0(self):
        self.calc.restar(2, 2)
        self.assertEqual(self.calc.get_resultado(), 0)

    def test_resta_3_menos_1_igual_2(self):
        self.calc.restar(3, 1)
        self.assertEqual(self.calc.get_resultado(), 2)

    def test_resta_menos_1_menos_2_igual_menos_3(self):
        self.calc.restar(-1, 2)
        self.assertEqual(self.calc.get_resultado(), -3)

    def test_resta_0_menos_menos_2_igual_2(self):
        self.calc.restar(0, -2)
        self.assertEqual(self.calc.get_resultado(), 2)

    def test_resta_a_menos_menos_1_datos_invalidos(self):
        self.calc.restar('a', 1)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    def test_resta_a_menos_menos_1_datos_invalidos(self):
        self.calc.restar(1, 'a')
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método multiplicar

    def test_multiplicacion_2_por_2_igual_4(self):
        self.calc.multiplicar(2, 2)
        self.assertEqual(self.calc.get_resultado(), 4)

    def test_multiplicacion_3_por_3_igual_9(self):
        self.calc.multiplicar(3, 3)
        self.assertEqual(self.calc.get_resultado(), 9)

    def test_multiplicacion_menos_3_por_4_igual_menos_12(self):
        self.calc.multiplicar(-3, 4)
        self.assertEqual(self.calc.get_resultado(), -12)

    def test_multiplicacion_3_por_menos_4_igual_menos_12(self):
        self.calc.multiplicar(3, -4)
        self.assertEqual(self.calc.get_resultado(), -12)

    def test_multiplicacion_menos_3_por_menos_4_igual_12(self):
        self.calc.multiplicar(-3, -4)
        self.assertEqual(self.calc.get_resultado(), 12)

    def test_multiplicacion_0_por_2_igual_0(self):
        self.calc.multiplicar(0, 2)
        self.assertEqual(self.calc.get_resultado(), 0)

    def test_multiplicacion_a_por_1_datos_invalidos(self):
        self.calc.multiplicar('a', 1)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    def test_multiplicacion_1_por_a_datos_invalidos(self):
            self.calc.multiplicar(1, 'a')
            self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método dividir

    # Pruebas del método raiz

    # Pruebas del método potencia


# Ejecuta las pruebas implementadas

if __name__ == '__main__':
    unittest.main()
