# Ejercicos 1.2 calculadora basica: Desarrollar una calculadora simple que solicite al usuario dos numero y una operacion matematica (+, -, *, /). El algoritmo debe realizar la operacion correspondiente y mostar el resultado. incluir validacion para evitar la division por cero, mostrando un mensaje de error en ese caso.

print("===========================")
print("calculadora basica")
print("creado por: jostin bedoya")
print("==========================='\n")

print("operaciones : +, -, *, /")
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
operacion = input("ingrese la operacion matematica: ")

if operacion == "+":
    resultado = num1 + num2
    print(f"el resultado de {num1} + {num2} es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"el resultado de {num1} - {num2} es: {resultado}")   
elif operacion == "*":
    resultado = num1 * num2
    print(f"el resultado de {num1} * {num2} es: {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"el resultado de {num1} / {num2} es: {resultado}")
    else:
        print("error: no se puede dividir por cero")
else:
    print("operacion no valida")