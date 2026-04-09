while True:
    print("\nCALCULADORA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 5:
        print("Saliendo de la calculadora...")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        print("Resultado:", num1 + num2)
    elif opcion == 2:
        print("Resultado:", num1 - num2)
    elif opcion == 3:
        print("Resultado:", num1 * num2)
    elif opcion == 4:
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("No se puede dividir por cero.")
    else:
        print("Opción no válida.")