# coding=utf-8

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def get_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        self.resultado = num1 + num2
