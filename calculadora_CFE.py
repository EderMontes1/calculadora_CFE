#calculadora Tarifas CFE
#Solo tarifa domestica, falta DAC

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
import sys


#Se agrega clase 
class crearVentana(tk.Tk):
    def __init__(self): #Se declara metodo init
        super().__init__() #Se inicializa el metodo super para llamar a la clase Padre
        
        #variables
        self.consumoBimestral = tk.IntVar(value="")
        self.pagoTotal = tk.IntVar(value="")
        self.tarifaBasico = 1.023 * 75
        self.tarifaIntermedio = 1.247 * 65
        self.tarifaExcedente = 3.646
        self.iva_vigente = 0.16
       
        

        #Se modifica el tamaño de ventana
        self.geometry("400x300")

        #Se modifica el titulo de la ventana
        self.title("Calculadora CFE")
        self.resizable(0,0)#Bloquear ventana 
        self._crearComponentes()
        self.crear_menu()
        

    def _crearComponentes(self):
        titulo = ttk.Label(self, text="Calculadora Consumo CFE" , font=16).place(x=110, y=30)
        etiqueta_Inicial = ttk.Label(self, text="Ingresa tu consumo inicial:").place(x=100, y=80)
        etiqueta_Final = ttk.Label(self, text="Ingresa tu consumo final:").place(x=100, y=120)
        etiqueta2 = ttk.Label(self, text="Tu consumo bimestral es de: ").place(x=100, y=170)
        etiqueta3 = ttk.Label(self, text="Tu total a pagar aproximado es de: ").place(x=100, y=200)

        #Boton Entry (Se debe separar el .place en 2 lineas o dara como resultado un error)
        self.entrada_inicial = ttk.Entry(self, width=4, justify=tk.CENTER)
        self.entrada_inicial.place(x=280, y=80)

        self.entrada_final = ttk.Entry(self, width=4, justify=tk.CENTER)
        self.entrada_final.place(x=280, y=120)
        
        #Boton Calcular
        boton_calcular = ttk.Button(self, text="Calcular consumo", command=self.enviar).place(x=150, y=250)
        
        etiqueta_consumobimestral = ttk.Label(self, textvariable=self.consumoBimestral).place(x=285, y=170)
        etiqueta_pagototal = ttk.Label(self, textvariable=self.pagoTotal).place(x=300, y=200)
        

    def enviar(self):
        consumoMensual = int(self.entrada_final.get()) - int((self.entrada_inicial.get()))
        self.consumoBimestral.set(consumoMensual)
        
        if self.consumoBimestral.get() >= 140: #Tarifa  Mayor a 140 KwH
            self.pago = float((self.tarifaBasico + self.tarifaIntermedio) + (self.tarifaExcedente * (self.consumoBimestral.get() - 140)))
            
        elif self.consumoBimestral.get() > 0 and self.consumoBimestral.get() < 76: #Tarifa > 0 y < 76 KwH
            self.pago = float((self.consumoBimestral.get() * 1.023))
        elif self.consumoBimestral.get() > 75 and self.consumoBimestral.get() < 140: #Tarifa >75 y < 140 KwH
            self.pago = float((self.tarifaBasico) + (self.consumoBimestral.get() - 75) * 1.24)
       
        return self.pagoTotal.set(round(float(self.pago * self.iva_vigente + (self.pago)),2)) #(Pago * IVA) + Pago Y se asigna el valor a la variable de la etiqueta pago total.
    
    def crear_menu(self):
        menu_principal = Menu(self)
        submenu_archivo = Menu(menu_principal, tearoff=0)
        submenu_archivo.add_command(label="Salir", command=self.salir)
        menu_principal.add_cascade(menu=submenu_archivo, label="Archivo")
        self.config(menu=menu_principal)
        
    def salir(self):
        self.quit() #Cerrar Ventana
        self.destroy() #Destruye Objeto
        sys.exit() #Termina el proceso
        

if __name__== "__main__":
    login_ventana = crearVentana()
    login_ventana.mainloop()
   
    

    

