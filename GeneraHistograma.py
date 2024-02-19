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
