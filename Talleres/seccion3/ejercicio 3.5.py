numeros = []
sin_duplicados = []

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)