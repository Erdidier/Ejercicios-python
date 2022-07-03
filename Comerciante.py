costo_inicial = 240.00
porcentaje_descuento = 0.25
porcentaje_aumento = 0.25

def calcular_descuento(costo,porcentaje):
    return costo - (costo * porcentaje)

def calcular_aumento(costo,porcentaje):
    return costo + (costo * porcentaje)

costo_compra = calcular_descuento(costo_inicial,porcentaje_descuento)
costo_venta = calcular_aumento(costo_compra,porcentaje_aumento)

print("El costo en el que se compró el producto es de:", costo_compra)
print("El costo en el que se vendió el producto es de:", costo_venta)