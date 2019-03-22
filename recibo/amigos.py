#esto es estructurado
numero = 3738
suma = 0
"""la letra i solo define un valor, puede ser cualquier letra"""
for i in range(1, numero, 1):
    if (numero % i) ==0:
        print (i, 'es divisor')
        suma += i
print ('la suma de los divisores es: ', suma)


