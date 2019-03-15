"""
>>> Cuota = Cuota(100000,10,24)
>>> Cuota.CalcularCuotaMensual()
>>> Cuota.getCuotaMensual()
11129.977635068779

>>> Cuota.getPagoTotal()
267119.4632416507
"""

class Cuota:
    __CapitalPrestado = float(0)
    __plazo = float(0)
    __ratio = float(0)
    __cuota = float(0)
    __PagoTotal = float(0)

    def __init__(self,CapitalPrestado,ratio,plazo):
        self.__CapitalPrestado = CapitalPrestado
        self.__ratio = ratio
        self.__plazo = plazo

    def CalcularCuotaMensual(self):
        self.__cuota = (self.__CapitalPrestado*self.__ratio)/(100*(1-((1+(self.__ratio/100))**(-self.__plazo))))
        self.__PagoTotal = self.__cuota*self.__plazo

    def getCuotaMensual(self):
        return self.__cuota
    def getPagoTotal(self):
        return self.__PagoTotal

if __name__ == '__main__':
    import doctest
    doctest.testmod()