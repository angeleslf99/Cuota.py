#nueva clase llamada Interfaz Circulo
#respetar la indentacion
#-*- coding: utf-8 -*-
#importa las clases de la libreria TKInter

from TKinter import *
from TKinder import ttk
class CirculoWindow():

    # metodoconstructor
    def __init__(self, window):
        self.window = window
        self.window.configure(bg='white')
        self.window.title('circulo')

        # se crea un frame container
        frame = LabelFrame(self.window, text='Calcular el área y perimetro')
        frame.grid(row=0, column=0, columnspam=4, padx=20, pady=20)

        # AGREGAR UN LABEL (ETIQUETA)
        Label(frame, text='Radio: ').grid(row=1, column=0)

        # AGREGAR UN TEXTBOX (CAJA DE TEXTO)
        # el focus es para agregar la iluminacion en la primera columna, por estetica, solo va en el primero
        # el row indica el valor de la fila, ejemplo si tengo 3 valores, el row va cambiando
        # y el focus se va a quitar, solo en el primero, e ire agregando a, b, c
        self.radio = Entry(frame)
        self.radio.focus()
        self.radio.grid(row= 1, column = 1)
        # Output - datos de salida

        #agregar un label
        Label(frame, text = 'Area: ').grid(row = 2, column = 0 )

        #agregar mensaje de salida
        self.area = Label(frame, text = '', fg = 'blue')
        self.area.grid(row = 2, column = 1)

        # agregar un label
        Label(frame, text='Perimetro: ').grid(row = 3, column = 0)

        # agregar mensaje de salida
        self.perimetro = Label(frame, text= '', fg='red')
        self.perimetro.grid(row = 3, column = 1)

        #AGREGAR BOTONES
        ttk.Button(frame, text = 'calcular', command = self.calcular).grid(row =4, column = 0)
        ttk.button(frame, text = 'salir', commnand = quit).grid(row = 4, column = 1)



    def validacion(self):
        return len(self.radio.get()) != 0

    def calcular(self):
        if self.validacion():
            try:
                radio = float(self.radio.get())
            except ValueError:
                self.area['text'] = 'El radio debe ser un numero'
        else:
            self.area['text'] = 'El radio esta vacio'


            # metodo main
    def main():
        window = TK()
        mi_programa = Circulo(Window)
        window.mainloop()
        return 0

    if __name__ == '__main__':
            main






