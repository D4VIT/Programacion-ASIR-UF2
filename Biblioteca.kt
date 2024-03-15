class Libro(val titulo: String, val autor: String, var exemplaresDisponibles: Int) {
    fun prestar() {
        if (exemplaresDisponibles > 0) {
            exemplaresDisponibles--
        }
    }

    fun retornar() {
        exemplaresDisponibles++
    }

    fun informacion(): String {
        return "Libro: $titulo, Autor: $autor, Ejemplares Disponibles: $exemplaresDisponibles"
    }
}

class Socio(val nombre: String, val apellido: String, val numeroSocio: Int) {
    fun solicitarPrestamo() {
        //e
    }

    fun retornarPrestamo() {
        //e
    }

    fun informacion(): String {
        return "Socio: $nombre $apellido, Numero de socio: $numeroSocio"
    }
}

class Prestamo(val libro: Libro, val socio: Socio, val fechaPrestamos: String) {
    
}














fun main() {
    val libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 2)
    val libro2 = Libro("Harry Potter", "J.K. Rowling", 3)

    val socio1 = Socio("Juan", "Perez", 1)
    val socio2 = Socio("María", "García", 2)

    val prestamo1 = Prestamo(libro1, socio1, "01/10/2021")
    val prestamo2 = Prestamo(libro2, socio2, "02/10/2021")

    println(libro1.informacion())
    println(socio1.informacion())
    println(prestamo1.informacion())
}
