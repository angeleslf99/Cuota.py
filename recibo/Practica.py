from NumeroEntre import NumeroEntre
angi = NumeroEntre(5.555)
angi.NumeroEntre()
print('Tu numero tiene: ',angi.getCantidadCifras(),' cifras')

from Recibo import Recibo
recibo = Recibo(12.16, 1200, 800)
recibo.calcularCosto()
print ('El pago del recibo es de: ', recibo.getTotalAPagar())

recibo2 = Recibo(9, 100, 300)
recibo2.calcularCosto()
print ('El pago del segundo recibo es de: ', recibo2.getTotalAPagar())


