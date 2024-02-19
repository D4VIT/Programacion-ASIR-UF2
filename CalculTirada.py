def calcular_probabilitat(valor):
    if valor < 2 or valor > 12:
        print("El valor no es entre 2 i 12.")
        return
    

    comptador = 0
    for tirada in range(2, 13):
        if tirada <= valor:
            comptador += tirades[tirada - 2]

    probabilitat = comptador * 100 / sum(tirades)
    print(f"La probabilitat es {probabilitat}%.")

tirades = [0] * 11
