"""
>>> Cuota = Cuota(100000,10,24)
>>> Cuota.CalcularCuotaMensual()
>>> Cuota.getCuotaMensual()
11129.977635068779

>>> Cuota.getPagoTotal()
267119.4632416507
"""
"""
Escribir un programa de un préstamo hipotecario (capital prestado,
interés anual y años que dura el préstamo) y le muestre la cuota 
mensual que habrá que pagar y el total de lo pagado una vez terminado 
el plazo, distinguiendo la cantidad de amortización y la de intereses
"""
class Cuota:
    __CapitalPrestado = float(0)
    __plazo = float(0)
    __ratio = float(0)
    __cuota = float(0)
    __PagoTotal = float(0)

#declaramos el método constructor
    def __init__(self,CapitalPrestado,ratio,plazo):
        self.__CapitalPrestado = CapitalPrestado
        self.__ratio = ratio
        self.__plazo = plazo

    """formulamos el método, en el cual, estamos dandole valor a nuestros atributos 
    y de esa manera poder aplicar la fórmula"""

    def CalcularCuotaMensual(self):
        self.__cuota = (self.__CapitalPrestado*self.__ratio)/(100*(1-((1+(self.__ratio/100))**(-self.__plazo))))
        self.__PagoTotal = self.__cuota*self.__plazo

    def getCuotaMensual(self):
        return self.__cuota
    def getPagoTotal(self):
        return self.__PagoTotal

    """ hacemos las pruebas unitarias para corroborar los resultados esperados
    y verificar si no hay errores"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()