suma = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("Suma total:", suma)