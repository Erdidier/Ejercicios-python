produccion_inicial = 1136.4
porcentaje = 0.165

def calcular_descuento(produccion,porcentaje):
    return produccion - (produccion * porcentaje)

produccion_2019 = calcular_descuento(produccion_inicial,porcentaje)
aumento = produccion_inicial - produccion_2019

print("La producción de salmón del 2019 fue de: US$", produccion_2019)
print("Y se tuvo un aumento del 2019 al 2020 de: US$", aumento)