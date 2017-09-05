# coding=utf-8

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def get_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        if not isinstance(num1, (int, float)) \
                or not isinstance(num2, (int, float)):
            self.resultado = 'Datos inválidos'
        else:
            self.resultado = num1 + num2
