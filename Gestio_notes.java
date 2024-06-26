class GestorNotes {
    private String[] nomsAlumnes;
    private int[][] notesAlumnes;

    public GestorNotes(int numAlumnes, int numAssignatures) {
        this.nomsAlumnes = new String[numAlumnes];
        this.notesAlumnes = new int[numAlumnes][numAssignatures];
    }

    public void registrarNotes(String nomAlumne, int[] notes) {
        for (int i = 0; i < nomsAlumnes.length; i++) {
            if (nomsAlumnes[i] == null) {
                nomsAlumnes[i] = nomAlumne;
                notesAlumnes[i] = notes;

                System.out.println("Notes de l'alumne" + nomAlumne + "Registrades amb exit.");
                return;
            }
        }
        System.out.println("No es poden registrar mes alumnes.");
    }

    public int[] obtenirNotes(String nomAlumne) {
        for (int i = 0; i < nomsAlumnes.length; i++) {
            if (nomsAlumnes[i] !=null && nomsAlumnes[i].equals(nomAlumne)) {
                return notesAlumnes[i];
            }
        }
        System.out.println("L'alumne" + nomAlumne + "no existeix.");
        return null;
    }
}

class CalculadoraEstadistiques {

}
