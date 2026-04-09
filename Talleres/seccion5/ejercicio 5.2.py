def calcular_promedio(lista):
    if len(lista) == 0:
        return "La lista está vacía."
    return sum(lista) / len(lista)

numeros = input("Ingrese números separados por comas: ")
lista = [float(num) for num in numeros.split(",")] if numeros else []

print("Promedio:", calcular_promedio(lista))