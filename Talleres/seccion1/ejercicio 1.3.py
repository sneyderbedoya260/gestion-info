# Ejercicio 1.3 - validacion de correo electronico: Crear un programa que pida al usuario ingresar un correo electronico y verifique que cntenga los caracteres "@" y "." en posiciones 
print("===========================")
print("validacion de correo electronico")               
print("creado por: jostin bedoya")
print("==========================='\n")

correo = input("ingrese su direccion de correo electronico: ")
if "@" in correo and "." in correo:
    print("direccion de correo electronico valida")
else:
    print("direccion de correo electronico no valida")
