data class Coordenada(val x: Int, val y: Int)

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

fun executarMoviment(coordenada: Coordenada, moviment: String): Coordenada {
    if (moviment == "dreta") {
        return moureDreta(coordenada)
    } else if (moviment == "esquerra") {
        return moureEsquerra(coordenada)
    } else if (moviment == "amunt") {
        return moureAmunt(coordenada)
    } else if (moviment == "avall") {
        return moureAvall(coordenada)

    }
}

fun main() {
    var coordenada = Coordenada(0, 0)

    coordenada = executarMoviment(coordenada, "dreta")
    println("Nova coordenada despres de moure a la dreta: $coordenada")

    coordenada = executarMoviment(coordenada, "amunt")
    println("Nova coordenada despres de moure amunt: $coordenada")
}
