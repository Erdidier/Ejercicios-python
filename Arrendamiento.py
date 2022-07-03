porcentaje_aumento = 0.06
costo_final = 256068

def calcular_descuento(costo,porcentaje):
    return costo - (costo * porcentaje)

def arriendo_inicial(años,costo,porcentaje):
    inicial = costo
    for i in range(0,años):
        inicial = calcular_descuento(inicial,porcentaje)
    return inicial

costo_inicial = arriendo_inicial(3,costo_final,porcentaje_aumento)

print("El valor inicial del arreindo fue de $", costo_inicial)