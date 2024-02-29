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