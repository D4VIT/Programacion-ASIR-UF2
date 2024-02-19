def generar_tirada():
    seed = 12345
    seed = (1103515245 * seed + 12345) % (2**31 - 1)
    return (seed % 6) + 1 + (seed // 6) % 6 + 1

def generar_histograma(num_tirades):
    histograma = [0] * 11
    for _ in range(num_tirades):
        tirada = generar_tirada()
        histograma[tirada - 2] += 1
    return histograma

def imprimir_histograma(histograma):
    max_repeticions = max(histograma)
    print("Histograma:")
    for i, repeticions in enumerate(histograma, start=2):
        print(f"{i}: {'*' * repeticions}")
    print(f"El maxim es {histograma.index(max_repeticions) +2} amb {max_repeticions} repeticions.")

tirades = 1000
histograma = generar_histograma(tirades)
imprimir_histograma(histograma)