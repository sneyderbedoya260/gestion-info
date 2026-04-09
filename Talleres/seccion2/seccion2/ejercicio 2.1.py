edad = int(input("Ingrese la edad: "))

if 0 <= edad <= 12:
    print("Es un niño.")
elif 13 <= edad <= 17:
    print("Es un adolescente.")
elif 18 <= edad <= 64:
    print("Es un adulto.")
elif edad >= 65:
    print("Es un adulto mayor.")
else:
    print("Edad no válida.")