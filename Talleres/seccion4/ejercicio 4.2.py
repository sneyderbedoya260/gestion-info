directorio = {}

while True:
    print("\n--- DIRECTORIO DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        directorio[nombre] = telefono
        print("Contacto agregado.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in directorio:
            print("Teléfono:", directorio[nombre])
        else:
            print("Contacto no encontrado.")

    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")
        if nombre in directorio:
            del directorio[nombre]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")

    elif opcion == "4":
        break

    else:
        print("Opción inválida.")