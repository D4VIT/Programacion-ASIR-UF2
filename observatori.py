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
