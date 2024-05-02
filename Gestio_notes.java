class GestorNotes {
    private String[] nomsAlumnes;
    private int[][] notesAlumnes;

    public GestorNotes(int numsAlumnes, int numAssignatures) {
        this.nomsAlumnes = new String[numAlumnes];
        this.notesAlumnes = new int[numAlumnes][numAssignatures];
    }

    public void registrarNotes(String nomAlumne, int[] notes) {
        for (int i = 0; i < nomsAlumnes.length; i++) {
            if (nomsAlumnes[i] == null) {
                nomsAlumnes[i] = nomAlumne;
                notesAlumnes[i] = notes;
            }
        }
    }
}
