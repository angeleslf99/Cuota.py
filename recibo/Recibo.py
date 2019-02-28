"""
>>>recibo = Recibo(12.16, 1200, 800)
>>>recibo.calcularCosto()
>>>recibo.getTotalAPagar()
5934.08
"""


class Recibo:
    __costoKw = float(0)
    __lecturalActual = float(0)
    __lecturaAnterior = float(0)
    __consumoKw = float(0)
    __totalAPagar = float(0)

    def __init__(self, costoKw, lecturaActual, lecturaAnterior):
        self.__costoKw = costoKw
        self.__lecturaAnterior = lecturaAnterior
        self.__lecturalActual = lecturaActual

    def calcularCosto(self):
        self.__consumoKw = self.__lecturalActual - self.__lecturaAnterior
        if (self.__consumoKw < 501):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.22
        if (self.__consumoKw > 500 & self.__consumoKw < 901):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.18
        if (self.__costoKw > 900):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.12

    def getTotalAPagar(self):
        return self.__totalAPagar