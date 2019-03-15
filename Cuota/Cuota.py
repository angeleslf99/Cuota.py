"""
>>> Cuota = Cuota(100000,10,24)
>>> Cuota.CalcularCuotaMensual()
>>> Cuota.getCuotaMensual()
11129.977635068779

>>> Cuota.getPagoTotal()
267119.4632416507
"""

class Cuota:
    __capital = float(0)
    __plazo = float(0)
    __ratio = float(0)
    __cuota = float(0)
    __total = float(0)

    def __init__(self,capital,ratio,plazo):
        self.__capital = capital
        self.__ratio = ratio
        self.__plazo = plazo

    def CalcularCuotaMensual(self):
        self.__cuota = (self.__capital*self.__ratio)/(100*(1-((1+(self.__ratio/100))**(-self.__plazo))))
        self.__total = self.__cuota*self.__plazo

    def getCuotaMensual(self):
        return self.__cuota
    def getPagoTotal(self):
        return self.__total

if __name__ == '__main__':
    import doctest
    doctest.testmod()