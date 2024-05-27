// Classe base Empleat
public class Empleat {
    protected String nom;
    protected double salari;

    public Empleat(String nom, double salari) {
        this.nom = nom;
        this.salari = salari;
    }

    public void imprimirDetalls() {
        System.out.println("Nom: " + nom);
        System.out.println("Salari: " + salari);
    }
}

// Classe filla EmpleatPerHores
public class EmpleatPerHores extends Empleat {
    private int horesTreballades;
    private double tarifaPerHora;

    public EmpleatPerHores(String nom, double tarifaPerHora, int horesTreballades) {
        super(nom, 0); // El salari es calcularà en el mètode calcularSalari()
        this.horesTreballades = horesTreballades;
        this.tarifaPerHora = tarifaPerHora;
    }

    public double calcularSalari() {
        salari = horesTreballades * tarifaPerHora;
        return salari;
    }
}

// Classe filla EmpleatAsalariat
public class EmpleatAsalariat extends Empleat {
    public EmpleatAsalariat(String nom, double salari) {
        super(nom, salari);
    }
}

// Classe filla EmpleatPerComisio
public class EmpleatPerComisio extends Empleat {
    private double vendesRealitzades;
    private double comisioPerVenta;

    public EmpleatPerComisio(String nom, double salari, double vendesRealitzades, double comisioPerVenta) {
        super(nom, salari); // Salari base
        this.vendesRealitzades = vendesRealitzades;
        this.comisioPerVenta = comisioPerVenta;
    }

    public double calcularSalari() {
        salari = salari + (vendesRealitzades * comisioPerVenta);
        return salari;
    }
}

// Classe Main per provar les classes
public class Main {
    public static void main(String[] args) {
        // Crear instàncies dels diferents tipus d'empleats
        EmpleatPerHores empleatPerHores = new EmpleatPerHores("Joan", 15.0, 160);
        EmpleatAsalariat empleatAsalariat = new EmpleatAsalariat("Maria", 2500.0);
        EmpleatPerComisio empleatPerComisio = new EmpleatPerComisio("Pere", 1800.0, 50000.0, 0.05);

        // Calcular i mostrar els salaris
        System.out.println("Salari empleat per hores: " + empleatPerHores.calcularSalari());
        System.out.println("Salari empleat assalariat: " + empleatAsalariat.salari);
        System.out.println("Salari empleat per comissió: " + empleatPerComisio.calcularSalari());

        // Mostrar els detalls dels empleats
        empleatPerHores.imprimirDetalls();
        empleatAsalariat.imprimirDetalls();
        empleatPerComisio.imprimirDetalls();
    }
}
