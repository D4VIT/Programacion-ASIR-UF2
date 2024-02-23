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
    pista = ''
    for i in range(len(combinacio_secreta)):
        if intent[i] == combinacio_secreta[i]:
            pista += 'O'
        elif
