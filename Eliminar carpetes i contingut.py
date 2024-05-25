'''
1.Obtener la ruta de la carpeta
1.1 leer la ruta de la carpeta
1.2 verificar que la ruta es correcta
1.3 Verificar que es una carpeta
2.Eliminar contenido de la carpeta
2.1Eliminar la carpeta
2.1.2 verificar que esta eliminada correctamente
'''
import os

# Funciones de gestión de empleados

def afegir_empleat(nom, cognom, edat, fitxer='empleats.txt'):
    with open(fitxer, 'a') as f:
        f.write(f"{nom},{cognom},{edat}\n")

def buscar_empleat(nom, fitxer='empleats.txt'):
    empleats = []
    with open(fitxer, 'r') as f:
        for linia in f:
            dades = linia.strip().split(',')
            if dades[0].lower() == nom.lower():
                empleats.append(dades)
    return empleats

def llistar_empleats(fitxer='empleats.txt'):
    empleats = []
    with open(fitxer, 'r') as f:
        for linia in f:
            dades = linia.strip().split(',')
            empleats.append(dades)
    return empleats

# Funciones de interacción con el usuario

def menu():
    print("1. Afegir Empleat")
    print("2. Buscar Empleat")
    print("3. Llistar Empleats")
    print("4. Sortir")
    return input("Seleccioneu una opció: ")

def main():
    while True:
        opcio = menu()
        if opcio == '1':
            nom = input("Introdueix el nom: ")
            cognom = input("Introdueix el cognom: ")
            edat = input("Introdueix l'edat: ")
            afegir_empleat(nom, cognom, edat)
            print("Empleat afegit correctament!")
        elif opcio == '2':
            nom = input("Introdueix el nom a buscar: ")
            empleats = buscar_empleat(nom)
            if empleats:
                for empleat in empleats:
                    print(f"Nom: {empleat[0]}, Cognom: {empleat[1]}, Edat: {empleat[2]}")
            else:
                print("No s'ha trobat cap empleat amb aquest nom.")
        elif opcio == '3':
            empleats = llistar_empleats()
            for empleat in empleats:
                print(f"Nom: {empleat[0]}, Cognom: {empleat[1]}, Edat: {empleat[2]}")
        elif opcio == '4':
            print("Sortint del programa.")
            break
        else:
            print("Opció no vàlida. Si us plau, seleccioneu una opció del menú.")

if __name__ == '__main__':
    main()
