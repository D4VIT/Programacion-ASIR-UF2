def generar_tirada():
    seed = 12345
    seed = (1103515245 * seed + 12345) % (2**31 - 1)
    return (seed % 6) + 1 + (seed // 6) % 6 + 1
