coordenada = (0, 0)

def moure(coordenada, direccio):
    x, y = coordenada
    if direccio == 'dreta':
        nova_coordenada = (x + 1, y)
    elif direccio == 'esquerra':
        nova_coordenada = (x - 1, y)
    elif direccio == 'amunt':
        nova_coordenada = (x, y + 1)
    elif direccio == 'avall':
        nova_coordenada = (x, y - 1)
    return nova_coordenada

coordenada = moure(coordenada, 'dreta')
print(f"Nova coordenada despres de moure a la dreta: {coordenada}")

coordenada = moure(coordenada, 'amunt')
print(f"Nova coordenada despres de moure amunt: {coordenada}")
