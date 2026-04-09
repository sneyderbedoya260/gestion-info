# ============================================
# MÓDULO 1: Servicio de datos
# Archivo: service.py
# Descripción: Maneja los datos en memoria
# ============================================

# ----- ESTRUCTURAS DE DATOS -----

# Lista para guardar todos los usuarios (cada usuario es un diccionario)
lista_usuarios = []

# Set para guardar IDs únicos (evita duplicados)
ids_registrados = set()


# ----- FUNCIONES DEL SERVICIO -----

def crear_usuario(id_usuario, nombre, email):
    """
    Crea un nuevo usuario y lo agrega a la lista.
    
    Parámetros:
        id_usuario: Identificador único
        nombre: Nombre del usuario
        email: Correo electrónico
    """
    # Crear el usuario como diccionario
    nuevo_usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "email": email
    }
    
    # Agregar a la lista de usuarios
    lista_usuarios.append(nuevo_usuario)
    
    # Agregar el ID al set de IDs registrados
    ids_registrados.add(id_usuario)
    
    print(f"Usuario '{nombre}' creado exitosamente.")


def listar_usuarios():
    """
    Muestra todos los usuarios registrados.
    """
    # Verificar si hay usuarios
    if len(lista_usuarios) == 0:
        print("No hay usuarios registrados.")
        return
    
    # Mostrar encabezado
    print("\n===== LISTA DE USUARIOS =====")
    print("-" * 40)
    
    # Recorrer y mostrar cada usuario
    for usuario in lista_usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Email: {usuario['email']}")
        print("-" * 40)
    
    # Mostrar total
    print(f"Total de usuarios: {len(lista_usuarios)}")


def obtener_ids():
    """
    Retorna el set de IDs registrados.
    Útil para las validaciones.
    """
    return ids_registrados