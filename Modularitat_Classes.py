coordenada = (0, 0)

def moure(coordenada, direccio):
    x, y = coordenada
    if direccio == 'dreta':
        nova_coordenada = (x + 1, y)
    elif direccio == 'esquerra':
        nova_coordenada = (x - 1, y)
