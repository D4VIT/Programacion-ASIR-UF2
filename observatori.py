def menu():
    print("Benvingut al registre de temperatures")
    print("--------------------------------------")
    print("[RT] Registrar temperatures setmanals")
    print("[MJ] Consultar temperatura mitjana")
    print("[DF] Consultar diferencia maxima")
    print("[FI] Sortir")

def registrar_temperatura():
    pregunta_temperatura = input("Escriu les temperatures d'aquesta setmana separades per espais: ")
    temperaturas = []
    tiempo = ''
    for caracter_actual in pregunta_temperatura:
        if caracter_actual != ' ':
            tiempo += caracter_actual
        else:
            temperaturas.append(float(tiempo))
            tiempo = ''
    if tiempo:
        temperaturas.append(float(tiempo))
    temperaturas.append(-1)

def calcular_diferencia_maxima():
    maxima_temperatura = -273.15
    minima_temperatura = 1000
    encontrado_marcador = 0
    diferencia_maxima = 0
    for tiempo in temperaturas:
        if tiempo == -1:
            encontrado_marcador = 1
        else:
            if tiempo > maxima_temperatura:
                maxima_temperatura = tiempo
            if tiempo < minima_temperatura:
                minima_temperatura = tiempo
    if encontrado_marcador == 1:
        diferencia_maxima = maxima_temperatura - minima_temperatura

def calcular_temperatura_media(temperaturas):
    suma = 0
    contador = 0
    for tiempo in temperaturas:
        if tiempo == -1:
            break
        suma += tiempo
        contador += 1
    if contador == 0:
        return 0
    return suma / contador
    
