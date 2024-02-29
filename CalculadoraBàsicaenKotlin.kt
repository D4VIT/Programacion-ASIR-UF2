fun sumar(numero1: Int, numero2: Int): Int {
    return numero1 + numero2
}

fun restar(numero1: Int, numero2: Int): Int {
    return numero1 - numero2
}

fun multiplicar(numero1: Int, numero2: Int): Int {
    return numero1 * numero2
}

fun dividir(numero1: Int, numero2: Int): Int? {
    return if (numero2 != 0) {
        numero1 / numero2
    } else {
        null
    }
}

fun main() {
    val a = 10
    val b = 5

    println("Suma: ${sumar(a, b)}")
    println("Resta: ${restar(a, b)}")
    println("Producte: ${multiplicar(a, b)}")

    val division = dividir(a, b)
    if (division != null) {
        println("Divisio: $division")
    } else {
        println("No es pot dividir per zero")
    }

}