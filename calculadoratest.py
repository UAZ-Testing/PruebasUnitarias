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

    def test_valor_inicio(self):
        self.assertEqual(self.calc.get_resultado(), 0)

    # Pruebas del método sumar

    def test_suma_positivos_1(self):
        self.calc.sumar(2, 2)
        self.assertEqual(self.calc.get_resultado(), 4)

    def test_suma_positivos_2(self):
        self.calc.sumar(3, 3)
        self.assertEqual(self.calc.get_resultado(), 6)

    def test_suma_con_cero(self):
        self.calc.sumar(0, 2)
        self.assertEqual(self.calc.get_resultado(), 2)

    def test_suma_negativos_1(self):
        self.calc.sumar(-1, 2)
        self.assertEqual(self.calc.get_resultado(), 1)

    def test_suma_datos_invalidos(self):
        self.calc.sumar('L', 2)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método restar

    def test_resta_positivos_1(self):
        self.calc.restar(2, 2)
        self.assertEqual(self.calc.get_resultado(), 0)

    def test_resta_positivos_2(self):
        self.calc.restar(3, 1)
        self.assertEqual(self.calc.get_resultado(), 2)

    def test_resta_negativos_1(self):
        self.calc.restar(-1, 2)
        self.assertEqual(self.calc.get_resultado(), -3)

    def test_resta_negativos_2(self):
        self.calc.restar(0, -2)
        self.assertEqual(self.calc.get_resultado(), 2)

    def test_resta_datos_invalidos_1(self):
        self.calc.restar('a', 1)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    def test_resta_datos_invalidos_2(self):
        self.calc.restar(1, 'a')
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método multiplicar

    def test_multiplicacion_positivos_1(self):
        self.calc.multiplicar(2, 2)
        self.assertEqual(self.calc.get_resultado(), 4)

    def test_multiplicacion_positivos_2(self):
        self.calc.multiplicar(3, 3)
        self.assertEqual(self.calc.get_resultado(), 9)

    def test_multiplicacion_negativos_1(self):
        self.calc.multiplicar(-3, 4)
        self.assertEqual(self.calc.get_resultado(), -12)

    def test_multiplicacion_negativos_2(self):
        self.calc.multiplicar(3, -4)
        self.assertEqual(self.calc.get_resultado(), -12)

    def test_multiplicacion_negativos_3(self):
        self.calc.multiplicar(-3, -4)
        self.assertEqual(self.calc.get_resultado(), 12)

    def test_multiplicacion_con_cero(self):
        self.calc.multiplicar(0, 2)
        self.assertEqual(self.calc.get_resultado(), 0)

    def test_multiplicacion_datos_invalidos_1(self):
        self.calc.multiplicar('a', 1)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    def test_multiplicacion_datos_invalidos_2(self):
        self.calc.multiplicar(1, 'a')
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método dividir

    def test_division_positivos_1(self):
        self.calc.dividir(4, 2)
        self.assertEqual(self.calc.get_resultado(), 2.0)

    def test_division_positivos_2(self):
        self.calc.dividir(3, 3)
        self.assertEqual(self.calc.get_resultado(), 1.0)

    def test_division_positivos_3(self):
        self.calc.dividir(3, 4)
        self.assertEqual(self.calc.get_resultado(), 0.75)

    def test_division_negativos_1(self):
        self.calc.dividir(-3, 4)
        self.assertEqual(self.calc.get_resultado(), -0.75)

    def test_division_negativos_2(self):
        self.calc.dividir(3, -4)
        self.assertEqual(self.calc.get_resultado(), -0.75)

    def test_division_negativos_3(self):
        self.calc.dividir(-3, -4)
        self.assertEqual(self.calc.get_resultado(), 0.75)

    def test_division_cero_numerador(self):
        self.calc.dividir(0, 2)
        self.assertEqual(self.calc.get_resultado(), 0.0)

    def test_division_cero_denominador(self):
        self.calc.dividir(2, 0)
        self.assertEqual(self.calc.get_resultado(),
                         'No se permiten divisiones entre 0')

    def test_division_datos_invalidos_1(self):
        self.calc.dividir('a', 1)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    def test_division_datos_invalidos_2(self):
        self.calc.dividir(1, 'a')
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método raiz

    def test_raiz_positivo_1(self):
        self.calc.raiz(2)
        self.assertEqual(self.calc.get_resultado(), 1.4142135623730951)

    def test_raiz_positivo_2(self):
        self.calc.raiz(9)
        self.assertEqual(self.calc.get_resultado(), 3.0)

    def test_raiz_positivo_3(self):
        self.calc.raiz(7)
        self.assertEqual(self.calc.get_resultado(), 2.6457513110645907)

    def test_raiz_negativo(self):
        self.calc.raiz(-5)
        self.assertEqual(self.calc.get_resultado(),
                         'No se permiten números negativos')

    def test_raiz_datos_invalidos(self):
        self.calc.raiz('a')
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    # Pruebas del método potencia

    def test_potencia_positivos_1(self):
        self.calc.potencia(2, 3)
        self.assertEqual(self.calc.get_resultado(), 8)

    def test_potencia_positivos_2(self):
        self.calc.potencia(9, 2)
        self.assertEqual(self.calc.get_resultado(), 81)

    def test_potencia_negativos_1(self):
        self.calc.potencia(-5, 2)
        self.assertEqual(self.calc.get_resultado(), 25)

    def test_potencia_negativos_2(self):
        self.calc.potencia(7, -2)
        self.assertEqual(self.calc.get_resultado(), 0.02040816326530612)

    def test_potencia_datos_invalidos_1(self):
        self.calc.potencia('a', 2)
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')

    def test_potencia_datos_invalidos_2(self):
        self.calc.potencia(1, 'a')
        self.assertEqual(self.calc.get_resultado(), 'Datos inválidos')


# Ejecuta las pruebas implementadas

if __name__ == '__main__':
    unittest.main()
