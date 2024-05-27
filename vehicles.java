public interface Vehicle {
    void accelerar(int velocitat);
    void frenar();
    int obtenerVelocidadActual();
}

class Automobil implements Vehicle {
    private String marcaModelo;
    private int velocidadActual;

    public Automobil(String marcaModelo) {
        this.marcaModelo = marcaModelo;
        this.velocidadActual = 0;
    }

    @Override
    public void accelerar(int velocitat) {
        this.velocidadActual += velocitat;
    }

    @Override
    public void frenar() {
        this.velocidadActual -= 10;
    }

    @Override
    public int obtenerVelocidadActual() {
        return velocidadActual;
    }
}

class Bicicleta implements Vehicle {
    private String tipo;
    private int velocidadActual;

    public Bicicleta(String tipo) {
        this.tipo = tipo;
        this.velocidadActual = 0;
    }

    @Override
    public void accelerar(int velocitat) {
        this.velocidadActual += velocitat;
    }

    @Override
    public void frenar() {
        this.velocidadActual -= 5;
    }

    @Override
    public int obtenerVelocidadActual() {
        return velocidadActual;
    }
}

public class Main {
    public static void main(String[] args) {
        Automobil miAuto = new Automobil("Toyota Corolla");
        Bicicleta miBicicleta = new Bicicleta("Montaña");

        miAuto.accelerar(50);
        miBicicleta.accelerar(20);

        System.out.println("Velocidad actual del automóvil: " + miAuto.obtenerVelocidadActual() + " km/h");
        System.out.println("Velocidad actual de la bicicleta: " + miBicicleta.obtenerVelocidadActual() + " km/h");

        miAuto.frenar();
        miBicicleta.frenar();

        System.out.println("Velocidad actual del automóvil después de frenar: " + miAuto.obtenerVelocidadActual() + " km/h");
        System.out.println("Velocidad actual de la bicicleta después de frenar: " + miBicicleta.obtenerVelocidadActual() + " km/h");
    }
}

