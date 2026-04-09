lista_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el producto: ")
        lista_compras.append(producto)
        print("Producto agregado.")

    elif opcion == "2":
        producto = input("Ingrese el producto a eliminar: ")
        if producto in lista_compras:
            lista_compras.remove(producto)
            print("Producto eliminado.")
        else:
            print("El producto no está en la lista.")

    elif opcion == "3":
        print("Lista actual:")
        for item in lista_compras:
            print("-", item)

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")