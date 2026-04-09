lista1 = input("Ingrese la primera lista separada por comas: ").split(",")
lista2 = input("Ingrese la segunda lista separada por comas: ").split(",")

comunes = []
unicos1 = []
unicos2 = []

for elemento in lista1:
    if elemento in lista2:
        comunes.append(elemento)
    else:
        unicos1.append(elemento)

for elemento in lista2:
    if elemento not in lista1:
        unicos2.append(elemento)

print("Elementos comunes:", comunes)
print("Únicos en lista 1:", unicos1)
print("Únicos en lista 2:", unicos2)