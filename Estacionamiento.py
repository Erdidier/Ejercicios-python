costo = 750
tiempo_minutos = 87
tiempo_intervalo = 30

def calcular_porcentaje(tiempo,intervalo):
    residuo = tiempo % intervalo
    porcentaje = (residuo * 100) / 30
    return porcentaje

def calcular_costo(costo,tiempo,intervalo,porcentaje=0.0):
    entero = int(tiempo / intervalo)
    print(entero)
    total = costo * entero
    if(entero * intervalo < tiempo):
        total += costo * porcentaje
    return total

porcentaje = calcular_porcentaje(tiempo_minutos,tiempo_intervalo) / 100
total = calcular_costo(costo,tiempo_minutos,tiempo_intervalo,porcentaje)

print("La persona debe cancelar la cantidad de $", total)