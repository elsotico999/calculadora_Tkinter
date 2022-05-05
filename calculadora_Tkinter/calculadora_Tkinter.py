import sys
import tkinter
from tkinter import *
from decimal import Decimal, getcontext
import math


def sumar():
    try:
        valor1 = float(entrada_texto.get())
        valor2 = float(entrada2_texto.get())
        valor = valor1 + valor2
        etiqueta3.config(text=round(valor,3))
    except ValueError:
        etiqueta3.config(text="Introduzca un número válido")

def restar():
    getcontext().prec = 3
    try:
        valor1 = float(entrada_texto.get())
        valor2 = float(entrada2_texto.get())
        valor = valor1 - valor2
        etiqueta4.config(text=round(valor,3))
    except ValueError:
        etiqueta4.config(text="Introduzca un número válido")

def multiplicar():
    getcontext().prec = 3
    try:
        valor1 = float(entrada_texto.get())
        valor2 = float(entrada2_texto.get())
        valor = valor1 * valor2
        etiqueta5.config(text=round(valor,3))
    except ValueError:
        etiqueta5.config(text="Introduzca un número válido")

def division():
    try:
        valor1 = float(entrada_texto.get())
        valor2 = float(entrada2_texto.get())
        valor = valor1 / valor2
        etiqueta6.config(text=round(valor,3))
    except ValueError:
        etiqueta6.config(text="Introduzca un número válido")

def raizcuadrada1():
    try:
        valor1 = float(entrada_texto.get())
        valor11 = math.sqrt(valor1)
        etiqueta7.config(text=round(valor11,3))
    except ValueError:
        etiqueta7.config(text="Introduzca un número válido")

def raizcuadrada2():
    try:
        valor2 = float(entrada2_texto.get())
        valor22 = math.sqrt(valor2)
        etiqueta8.config(text=round(valor22,3))
    except ValueError:
        etiqueta8.config(text="Introduzca un número válido")


app = Tk()
app.title("Operaciones con dos números")

# Ventana Principal
vp = Frame(app)
vp.grid(column=10, row=10, padx=(100, 100), pady=(30, 30))
vp.columnconfigure(0, weight=2)
vp.rowconfigure(0, weight=2)

etiqueta = Label(vp, text="Número 1")
etiqueta.grid(column=1, row=1, sticky=(W, E))
etiqueta2 = Label(vp, text="Número 2")
etiqueta2.grid(column=3, row=1, sticky=(W, E))

etiqueta3= Label(vp, text="Suma")
etiqueta3.grid(column=1, row=5, sticky=(W, E))
etiqueta4= Label(vp, text="Resta")
etiqueta4.grid(column=2, row=5, sticky=(W, E))
etiqueta5= Label(vp, text="Multiplicación")
etiqueta5.grid(column=3, row=5, sticky=(W, E))
etiqueta6= Label(vp, text="División")
etiqueta6.grid(column=4, row=5, sticky=(W, E))
etiqueta7= Label(vp, text="Raíz cuadrada número 1")
etiqueta7.grid(column=5, row=5, sticky=(W, E))
etiqueta8= Label(vp, text="Raíz cuadrada número 2")
etiqueta8.grid(column=6, row=5, sticky=(W, E))

boton = Button(vp, text="Sumar", command=sumar)
boton.grid(column=1, row=6)
boton2 = Button(vp, text="Restar", command=restar)
boton2.grid(column=2, row=6)
boton3= Button(vp, text="Multiplicar", command=multiplicar)
boton3.grid(column=3, row=6)
boton4= Button(vp, text="División", command=division)
boton4.grid(column=4, row=6)
boton5= Button(vp, text="Raíz cuadrada número 1", command=raizcuadrada1)
boton5.grid(column=5, row=6)
boton6= Button(vp, text="Raíz cuadrada número 2", command=raizcuadrada2)
boton6.grid(column=6, row=6)

valor = ""
entrada_texto = Entry(vp, width=30, textvariable=valor)
entrada_texto.grid(column=2, row=1)
valor2 = ""
entrada2_texto = Entry(vp, width=30, textvariable=valor2)
entrada2_texto.grid(column=4, row=1)


app.mainloop()