import java.util.ArrayList;
import java.util.List;

class Llibre {
    private String titol;

    public Llibre(String titol) {
        this.titol = titol;
    }

    public String getTitol() {
        return titol;
    }
}

class LlistaLlibres<T extends Llibre> {
    private List<T> llibres;

    public LlistaLlibres() {
        llibres = new ArrayList<>();
    }

    public void afegirLlibre(T llibre) {
        llibres.add(llibre);
    }

    public void eliminarLlibre(T llibre) {
        llibres.remove(llibre);
    }

    public T buscarLlibrePerTitol(String titol) {
        for (T llibre : llibres) {
            if (llibre.getTitol().equals(titol)) {
                return llibre;
            }
        }
        return null;
    }

    public void mostrarLlibres() {
        for (T llibre : llibres) {
            System.out.println(llibre.getTitol());
        }
    }
}
