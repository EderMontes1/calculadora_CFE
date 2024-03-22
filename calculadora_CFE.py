#calculadora Tarifas CFE

consumoMensual = (int(input("Ingresa tu consumo Mensual: ")))
consumoBimestre = consumoMensual * 2

tarifaBasico = 1.023 * 75
tarifaIntermedio = 1.247 * 65
tarifaExcedente = 3.646

print(f"Tu consumo al Bimestre es {consumoBimestre} kWh")

if consumoBimestre > 140:
    consumoTotal = (tarifaBasico + tarifaIntermedio) + (tarifaExcedente * (consumoBimestre - 140))
else:
    consumoTotal = (tarifaBasico + tarifaIntermedio)
    
print(f"Tu pago aproximado es de ${consumoTotal} pesos")
    

    
    