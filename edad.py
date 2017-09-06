# coding=utf-8

class Edad:
    def evaluar_edad(self, edad):
        if not isinstance(edad, (int, float)):
            return 'debes insertar un número'
        elif edad < 0:
            return 'no existes'
        elif edad == 0:
            return 'eres un recién nacido'
        elif edad < 13:
            return 'eres niño'
        elif edad < 18:
            return 'eres adolescente'
        elif edad < 65:
            return 'eres adulto'
        elif edad < 120:
            return 'eres adulto mayor'
        else:
            return 'eres Mumm-Ra'