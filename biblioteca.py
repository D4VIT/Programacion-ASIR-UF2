

'''
biblioteca = []

while True:
    print("\n1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        disponibilidad = True
        libro = {"titulo": titulo, "autor": autor, "genero": genero, "disponibilidad": disponibilidad}
        biblioteca.append(libro)
        print(f'Libro "{titulo}" agregado a la biblioteca.')

    elif opcion == "2":
        titulo = input("Ingrese el título del libro a prestar: ")
        encontrado = False
        for libro in biblioteca:
            if libro["titulo"] == titulo and libro["disponibilidad"]:
                libro["disponibilidad"] = False
                print(f'Libro "{titulo}" prestado con éxito.')
                encontrado = True
                break
        if not encontrado:
            print(f'Libro "{titulo}" no disponible para préstamo.')

    elif opcion == "3":
        titulo = input("Ingrese el título del libro a devolver: ")
        encontrado = False
        for libro in biblioteca:
            if libro["titulo"] == titulo and not libro["disponibilidad"]:
                libro["disponibilidad"] = True
                print(f'Libro "{titulo}" devuelto con éxito.')
                encontrado = True
                break
        if not encontrado:
            print(f'No se puede devolver el libro "{titulo}".')

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción correcta.")
'''
biblioteca = []
def mostrar_menu():
    print("\n1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")

def agregar_libro():
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        disponibilidad = True
        libro = {"titulo": titulo, "autor": autor, "genero": genero, "disponibilidad": disponibilidad}
        biblioteca.append(libro)
        print(f'Libro "{titulo}" agregado a la biblioteca.')

def prestar_libro():
        titulo = input("Ingrese el título del libro a prestar: ")
        encontrado = False
        for libro in biblioteca:
            if libro["titulo"] == titulo and libro["disponibilidad"]:
                libro["disponibilidad"] = False
                print(f'Libro "{titulo}" prestado con éxito.')
                encontrado = True
                break
        if not encontrado:
            print(f'Libro "{titulo}" no disponible para préstamo.')

def devolver_libro():
        titulo = input("Ingrese el título del libro a devolver: ")
        encontrado = False
        for libro in biblioteca:
            if libro["titulo"] == titulo and not libro["disponibilidad"]:
                libro["disponibilidad"] = True
                print(f'Libro "{titulo}" devuelto con éxito.')
                encontrado = True
                break
        if not encontrado:
            print(f'No se puede devolver el libro "{titulo}".')

def salir():
        print("Saliendo del programa.")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opcion de 1 a 4:")

    if opcion == "1":
         agregar_libro()
    elif opcion == "2":
         prestar_libro()
    elif opcion == "3":
         devolver_libro()
    elif opcion == "4":
         salir()
    else:
        print("Opción no válida. Por favor, seleccione una opción correcta.")