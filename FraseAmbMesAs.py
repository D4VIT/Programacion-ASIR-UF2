def FraseAmbMesAs():
    maximo_numero_de_a = 0
    frase_con_mas_a = ""

    while True:
        frase = input("Escriu una frase:\n> ")

        if frase == "fi":
            break

        numero_a = 0
        for caracter in frase:
            if caracter == 'a' or caracter == 'A':
