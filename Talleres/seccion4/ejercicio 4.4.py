numeros = input("Ingrese números separados por comas: ")
lista = [float(num) for num in numeros.split(",")]

maximo = max(lista)
minimo = min(lista)
suma = sum(lista)
promedio = suma / len(lista)

print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Suma total:", suma)
print("Promedio:", promedio)