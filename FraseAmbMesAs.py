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
                numero_a += 1

        if numero_a > maximo_numero_de_a:
            maximo_numero_de_a = numero_a
            frase_con_mas_a = frase

        
        print(f"La frase amb mes 'a' es: \"{frase_con_mas_a}\"")
        print(f"Te {maximo_numero_de_a} 'a'.")

FraseAmbMesAs()