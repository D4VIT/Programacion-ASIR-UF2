pizzas_disponibles = []

def mostrar_menu():
    print("\n1. Tomar pedido")
    print("2. Preparar pizza")
    print("3. Gestionar Estoc")
    print("4. Procesar Pago")
    print("5. Salir")

def tomar_pedido():
    print("Se esta haciendo un nuevo pedido")

def preparar_pizza():
    nombre_pizza = input("Ingrese el nombre de la pizza que quiere: ")
    pizzas_disponibles.append(nombre_pizza)
    print(f'Pizza "{nombre_pizza}" preparada...')

def gestionar_stock():
    print("Se gestiona el stock de ingredientes para la pizza")

def procesar_pago():
    print("Se procesa el pago.....")

def salir():
    print("Saliendo.....")

while True:
    mostrar_menu()
    opcion = input("Selecciona una: ")

    if opcion == "1":
        tomar_pedido()
    elif opcion == "2":
        preparar_pizza()
    elif opcion == "3":
        gestionar_stock()
    elif opcion == "4":
        procesar_pago()
    elif opcion == "5":
        salir()
    else:
        print("opcion no valida elige una de las 5")
