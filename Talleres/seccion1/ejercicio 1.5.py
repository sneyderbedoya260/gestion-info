print("MENÚ DE CONVERSIÓN")
print("1. Celsius a Fahrenheit")
print("2. Kilómetros a Millas")
print("3. Kilogramos a Libras")

opcion = int(input("Seleccione una opción (1-3): "))
valor = float(input("Ingrese el valor a convertir: "))

if opcion == 1:
    resultado = (valor * 9/5) + 32
    print(f"Resultado: {resultado:.2f} °F")
elif opcion == 2:
    resultado = valor * 0.621371
    print(f"Resultado: {resultado:.2f} millas")
elif opcion == 3:
    resultado = valor * 2.20462
    print(f"Resultado: {resultado:.2f} libras")
else:
    print("Opción no válida.")