while True:
    numero = int(input("Ingrese un número para ver su tabla: "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    opcion = input("¿Desea generar otra tabla? (s/n): ").lower()
    if opcion != "s":
        break