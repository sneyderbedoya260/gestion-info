def saludar(nombre, hora):
    if 5 <= hora <= 12:
        return f"Buenos días {nombre}"
    elif 13 <= hora <= 19:
        return f"Buenas tardes {nombre}"
    else:
        return f"Buenas noches {nombre}"

nombre = input("Ingrese su nombre: ")
hora = int(input("Ingrese la hora (0-23): "))
print(saludar(nombre, hora))