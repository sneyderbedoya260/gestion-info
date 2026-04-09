# ============================================
# MÓDULO 1: Validaciones
# Archivo: validate.py
# Descripción: Funciones para validar datos
# ============================================

def validar_id(id_valor, ids_existentes):
    """
    Valida que el ID no esté vacío y no exista ya.
    
    Parámetros:
        id_valor: El ID a validar
        ids_existentes: Set con los IDs que ya existen
    
    Retorna:
        True si es válido, False si no
    """
    # Verificar que no esté vacío
    if id_valor == "":
        print("Error: El ID no puede estar vacío.")
        return False
    
    # Verificar que no exista ya (usando el set)
    if id_valor in ids_existentes:
        print("Error: El ID ya existe.")
        return False
    
    return True


def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío.
    
    Parámetros:
        nombre: El nombre a validar
    
    Retorna:
        True si es válido, False si no
    """
    if nombre == "":
        print("Error: El nombre no puede estar vacío.")
        return False
    
    return True


def validar_email(email):
    """
    Valida que el email tenga formato básico (contenga @).
    
    Parámetros:
        email: El email a validar
    
    Retorna:
        True si es válido, False si no
    """
    if email == "":
        print("Error: El email no puede estar vacío.")
        return False
    
    if "@" not in email:
        print("Error: El email debe contener @.")
        return False
    
    return True