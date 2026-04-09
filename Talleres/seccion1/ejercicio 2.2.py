print("1. Saludar")
print("2. Despedirse")
print("3. Salir")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    print("¡Hola! ")
elif opcion == 2:
    print("¡Hasta luego! ")
elif opcion == 3:
    print("Programa finalizado.")
else:
    print("Opción no válida.")