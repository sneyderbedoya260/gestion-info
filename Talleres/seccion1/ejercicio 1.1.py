# Ejercicio 1.1 - Registro de usuaroio: crear un algoritmo que permita registrar los datos de un usuario. El programa debe solicitar: nombre, edad y ciudad de residencia. luego, mostrar un mensaje personalizado con el siguiente formato: "hola [nmbre], tienes [edad] años y vives en [ciudad]. " validar Validar que la edad sea un numero positivo

print("=============================================================")
print("Registro de usuario")
print("Creado por jostin bedoya")
print("=============================================================")

nombre = input("ingrese su nombre")
edad = int(input("ingrese su edad"))
ciudad = input("ingrese su ciudad de nacimiento ")

if edad > 0: 
    print(f"hola {nombre}, tienes {edad} años y vives en {ciudad},")

else: 
    print("tienes una edad no validad ")