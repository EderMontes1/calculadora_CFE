#calculadora Tarifas CFE
#Solo tarifa domestica, falta DAC

import tkinter as tk
from tkinter import ttk
from tkinter import *

#Se crea el objeto
ventana = tk.Tk()

#Se modifica el tamaño de ventana
ventana.geometry("400x300")

#Se modifica el titulo de la ventana
ventana.title("Calculadora CFE")

titulo = ttk.Label(ventana, text="Calculadora Consumo CFE" , font=16).place(x=110, y=30)
etiqueta = ttk.Label(ventana, text="Ingresa tu consumo mensual:").place(x=100, y=80)
etiqueta2 = ttk.Label(ventana, text="Tu consumo bimestral es de: ").place(x=100, y=120)
etiqueta3 = ttk.Label(ventana, text="Tu total a pagar aproximado es de: ").place(x=100, y=150)

consumoBimestral = tk.IntVar(value="")
pagoTotal = tk.IntVar(value="")

tarifaBasico = 1.023 * 75
tarifaIntermedio = 1.247 * 65
tarifaExcedente = 3.646

#Boton Entry (Se debe separar el .place en 2 lineas o dara como resultado un error)
entrada = ttk.Entry(ventana, width=4, justify=tk.CENTER)
entrada.place(x=280, y=80)

def enviar():
    consumoMensual = int(entrada.get()) * 2
    consumoBimestral.set(consumoMensual)
    
    if consumoBimestral.get() > 140:
        pago = float((tarifaBasico + tarifaIntermedio) + (tarifaExcedente * (consumoBimestral.get() - 140)))
    elif consumoBimestral.get() > 0 and consumoBimestral.get() < 76:
        pago = float((consumoBimestral.get() * 1.023))
    elif consumoBimestral.get() > 75 and consumoBimestral.get() < 140:
        pago = float((tarifaBasico) + ((consumoBimestral.get() - 75) * 1.2470))
    return pagoTotal.set(pago)
    
etiqueta_consumobimestral = ttk.Label(ventana, textvariable=consumoBimestral).place(x=270, y=120)
etiqueta_pagototal = ttk.Label(ventana, textvariable=pagoTotal).place(x=300, y=150)

#Boton Calcular
boton_calcular = ttk.Button(ventana, text="Calcular consumo", command=enviar).place(x=150, y=250)
#Layout Manager para desplegar botones

ventana.mainloop()  


