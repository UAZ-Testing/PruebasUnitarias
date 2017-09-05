# coding=utf-8

import math


class Calculadora:
    def __init__(self):
        self.resultado = 0

    def get_resultado(self):
        return self.resultado

    def sumar(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            self.resultado = num1 + num2
        else:
            self.resultado = 'Datos inválidos'

    def restar(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            self.resultado = num1 - num2
        else:
            self.resultado = 'Datos inválidos'

    def multiplicar(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            self.resultado = num1 * num2
        else:
            self.resultado = 'Datos inválidos'

    def dividir(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            try:
                self.resultado = num1 / num2
            except ZeroDivisionError:
                self.resultado = 'No se permiten divisiones entre 0'
        else:
            self.resultado = 'Datos inválidos'

    def raiz(self, num):
        if self.validar_tipo_datos(num):
            try:
                self.resultado = math.sqrt(num)
            except ValueError:
                self.resultado = 'No se permiten números negativos'
        else:
            self.resultado = 'Datos inválidos'

    def potencia(self, num1, potencia):
        if self.validar_tipo_datos(num1, potencia):
            self.resultado = num1 ** potencia
        else:
            self.resultado = 'Datos inválidos'

    def validar_tipo_datos(self, num1, num2=0):
        return isinstance(num1, (int, float)) and isinstance(num2, (int, float))
