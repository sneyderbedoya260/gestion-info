contraseña = input("Ingrese una contraseña: ")

errores = []

if len(contraseña) < 8:
    errores.append("Debe tener al menos 8 caracteres.")

if not any(c.isupper() for c in contraseña):
    errores.append("Debe contener al menos una letra mayúscula.")

if not any(c.isdigit() for c in contraseña):
    errores.append("Debe contener al menos un número.")

caracteres_especiales = "!@#$%^&*"
if not any(c in caracteres_especiales for c in contraseña):
    errores.append("Debe contener al menos un carácter especial (!@#$%^&*).")

if len(errores) == 0:
    print(" Contraseña segura.")
else:
    print(" La contraseña no cumple con los siguientes criterios:")
    for error in errores:
        print("-", error)