def moure_dreta(coordenada):
    x, y = coordenada
    nova_coordenada = (x + 1, y)
    return nova_coordenada

def moure_esquerra(coordenada):
    x, y = coordenada
    nova_coordenada = (x - 1, y)
    return nova_coordenada

def moure_amunt(coordenada):
    x, y = coordenada
    nova_coordenada = (x, y + 1)
    return nova_coordenada

def moure_avall(coordenada):
    x, y = coordenada
    nova_coordenada = (x, y - 1)
    return nova_coordenada

def executar_moviment(coordenada, moviment):
    if moviment == "dreta":
        return moure_dreta(coordenada)
    elif moviment == "esquerra":
        return moure_esquerra(coordenada)
    elif moviment == "amunt":
        return moure_amunt(coordenada)
    elif moviment == "avall":
        return moure_avall(coordenada)

coordenada = (0, 0)

coordenada = executar_moviment(coordenada, 'dreta')
print(f"Nova coordenada després de moure a la dreta: {coordenada}")

coordenada = executar_moviment(coordenada, "amunt")
print(f"Nova coordenada després de moure amunt: {coordenada}")

