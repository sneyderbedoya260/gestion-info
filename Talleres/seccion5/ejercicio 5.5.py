def factorial(n):
    if n < 0:
        return "No existe factorial para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))
print("Factorial:", factorial(numero))