def generar_combinacio_secreta():
    combinacio = ''
    lletres = 'abcdefghijklmnopqrstuvwxyz'
    seed = 12345
    for _ in range(5):
        index = seed % len(lletres)
        combinacio += lletres[index]
        seed //= 2
    return combinacio

def donar_pista(combinacio_secreta, intent):
