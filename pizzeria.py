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
    print("se prepara una pizza")

def gestionar_stock():
    print("Se gestiona el stock de ingredientes para la pizza")
