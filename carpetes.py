import os

class LimpiarCarpeta:
    def __init__(self):
        pass

    def obtener_ruta(self):
        ruta = input("Introduce la ruta de la carpeta existente: ")
        return ruta

    def limpiar_carpeta(self, ruta):
        if os.path.exists(ruta):
            for elemento in os.listdir(ruta):
                elemento_completo = os.path.join(ruta, elemento)
                if os.path.isfile(elemento_completo):
                    os.remove(elemento_completo)
                elif os.path.isdir(elemento_completo):
                    self.limpiar_carpeta(elemento_completo)
                    os.rmdir(elemento_completo)
            print(f"La carpeta {ruta} ha sido limpiada exitosamente.")
        else:
            print(f"La carpeta {ruta} no existe.")

if __name__ == "__main__":
    limpiador = LimpiarCarpeta()
    ruta_carpeta = limpiador.obtener_ruta()
    limpiador.limpiar_carpeta(ruta_carpeta)

