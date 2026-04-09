# ============================================
# MÓDULO 1: Programa Principal
# Archivo: main.py
# Descripción: Menú interactivo en consola
# ============================================

# Importar los módulos que creamos
from validate import validar_id, validar_nombre, validar_email
from service import crear_usuario, listar_usuarios, obtener_ids


def mostrar_menu():
    """
    Muestra el menú de opciones.
    """
    print("\n===== SISTEMA DE GESTIÓN =====")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Salir")
    print("=" * 30)


def opcion_crear_usuario():
    """
    Solicita datos y crea un nuevo usuario.
    """
    print("\n--- Crear Nuevo Usuario ---")
    
    # Pedir el ID
    id_usuario = input("Ingrese ID: ")
    
    # Validar el ID
    if not validar_id(id_usuario, obtener_ids()):
        return  # Salir si no es válido
    
    # Pedir el nombre
    nombre = input("Ingrese nombre: ")
    
    # Validar el nombre
    if not validar_nombre(nombre):
        return  # Salir si no es válido
    
    # Pedir el email
    email = input("Ingrese email: ")
    
    # Validar el email
    if not validar_email(email):
        return  # Salir si no es válido
    
    # Si todo es válido, crear el usuario
    crear_usuario(id_usuario, nombre, email)


def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Bienvenido al Sistema de Gestión de Usuarios")
    
    # Bucle principal del programa
    while True:
        # Mostrar menú
        mostrar_menu()
        
        # Pedir opción al usuario
        opcion = input("Seleccione una opción: ")
        
        # Evaluar la opción elegida
        if opcion == "1":
            opcion_crear_usuario()
        
        elif opcion == "2":
            listar_usuarios()
        
        elif opcion == "3":
            print("¡Hasta luego!")
            break  # Salir del bucle
        
        else:
            print("Opción no válida. Intente de nuevo.")


# ----- PUNTO DE ENTRADA -----
# Esto ejecuta el programa cuando se corre el archivo
if __name__ == "__main__":
    main()