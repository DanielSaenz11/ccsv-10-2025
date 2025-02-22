
carrito = []  # Lista para almacenar los productos
total = 0  # Variable para almacenar el total de la compra

while True:
    print("\nMenú del Carrito de Compras:")
    print("1. Agregar producto")
    print("2. Ver carrito y total")
    print("3. Eliminar producto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        producto = input("Nombre del producto: ")
        try:
            precio = float(input("Precio del producto: "))
            carrito.append((producto, precio))
            total += precio
            print(f"'{producto}' agregado con éxito.")
        except ValueError:
            print("⚠️ Error: Ingresa un precio válido.")
    
    elif opcion == "2":
        if len(carrito) == 0:
            print("El carrito está vacío.")
        else:
            print("\nProductos en el carrito:")
            for i, (producto, precio) in enumerate(carrito, start=1):
                print(f"{i}. {producto} - ${precio:.2f}")
            print(f"\nTotal a pagar: ${total:.2f}")
    
    elif opcion == "3":
        if len(carrito) == 0:
            print("No hay productos en el carrito para eliminar.")
        else:
            print("\nProductos disponibles:")
            for i, (producto, precio) in enumerate(carrito, start=1):
                print(f"{i}. {producto} - ${precio:.2f}")

            try:
                num = int(input("Número del producto a eliminar: ")) - 1
                if 0 <= num < len(carrito):
                    eliminado = carrito.pop(num)
                    total -= eliminado[1]
                    print(f"❌ '{eliminado[0]}' eliminado del carrito.")
                else:
                    print("⚠️ Número inválido.")
            except ValueError:
                print("⚠️ Ingresa un número válido.")
    
    elif opcion == "4":
        print("👋 Saliendo del programa...")
        break
    
    else:
        print("⚠️ Opción no válida. Intenta de nuevo.")
