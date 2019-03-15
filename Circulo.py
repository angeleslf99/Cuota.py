"""
>>> circulo = Circulo(2)
>>> circulo.getArea()
12.566370614359172
"""

import recibo

class Circulo:
    __radio = float(0)
    __perimetro = float(0)
    __area = float(0)

    def __init__(self, radio): # crearemos el metodo constructor, seguido de los metodos que deriva el problema
        if(radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self.__area = recibo.pi * (self.__radio * self.__radio)

    def calcularPerimetro(self):
        self.__perimetro = (2 * recibo.pi) * self.__radio

    def getArea(self):
        return self.__area

    def getPerimetro(self):
        return self.__perimetro

if __name__==  '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test.txt")