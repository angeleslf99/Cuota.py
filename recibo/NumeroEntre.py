class NumeroEntre:
    __numero = float(0)
    __cifras = int(0)

    def __init__(self, numero):
        self.__numero = numero
        return

    def NumeroEntre(self):
        if((self.__numero>=0) & (self.__numero<=9.999)):
            return 0

    def getCantidadCifras(self):
        return self.__cifras






