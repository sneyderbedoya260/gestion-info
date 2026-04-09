nombres = ["sofia", "felipe", "dieho", "isabela", "valentina"]

buscar = input("Ingrese el nombre a buscar: ")

encontrado = False

for i in range(len(nombres)):
    if nombres[i].lower() == buscar.lower():
        print(f"Nombre encontrado en la posición {i}.")
        encontrado = True
        break

if not encontrado:
    print("Nombre no encontrado.")