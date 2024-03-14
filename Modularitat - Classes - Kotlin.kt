fun moureDreta(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x + 1, coordenada.y)
}

fun moureEsquerra(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x - 1, coordenada.y)
}

fun moureAmunt(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x, coordenada.y + 1)
}

fun moureAvall(coordenada: Coordenada): Coordenada {
    return Coordenada(coordenada.x, coordenada.y - 1)
}


