'''creamos un metodo que nos pida un mumero entre en 0 y el 9,999 y decir cuantas cifras tiene'''

class NumeroEntre: #este es el nombre de nuestra clase
    __numero = float(0) #Declaramos los atributos
    __cifras = int(0)

    def __init__(self, numero): #declaramos el metodo constructor
        self.__numero = numero
        return 0

    def NumeroEntre(self):
        if((self.__numero>=0) & (self.__numero<=9.999)): #gregamos if para declarar entre que valores sera nuestro rango
         return 0

    def getCantidadCifras(self):
        return self.__cifras
        #esta es nuestra salida, como conclusion afirmo que el proposito de la unidad 1
        # y unidad 2 se ha cumplido, pues se trata de conocer cada uno de los elementos con los que trabajaremos





