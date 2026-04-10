"""
validate.py
Funciones de validacion de campos para registros de repuestos.
Cada funcion retorna (True, "") si es valido o (False, mensaje) si no.
"""

CATEGORIAS_VALIDAS: set[str] = {
    "motor",
    "frenos",
    "suspension",
    "electrico",
    "transmision",
    "carroceria",
    "filtros",
    "lubricacion",
}

MARCAS_MOTO_VALIDAS: set[str] = {
    "honda",
    "yamaha",
    "suzuki",
    "kawasaki",
    "bajaj",
    "tvs",
    "royal enfield",
    "ktm",
    "hero",
    "generica",
}


def validar_codigo(codigo: str) -> tuple[bool, str]:
    """Valida que el codigo sea alfanumerico y tenga entre 4 y 20 caracteres."""
    if not isinstance(codigo, str):
        return False, "El codigo debe ser una cadena de texto."
    codigo = codigo.strip()
    if len(codigo) < 4 or len(codigo) > 20:
        return False, "El codigo debe tener entre 4 y 20 caracteres."
    if not codigo.isalnum():
        return False, "El codigo solo puede contener letras y numeros, sin espacios ni simbolos."
    return True, ""


def validar_nombre(nombre: str) -> tuple[bool, str]:
    """Valida que el nombre tenga entre 3 y 100 caracteres."""
    if not isinstance(nombre, str):
        return False, "El nombre debe ser una cadena de texto."
    nombre = nombre.strip()
    if len(nombre) < 3:
        return False, "El nombre debe tener al menos 3 caracteres."
    if len(nombre) > 100:
        return False, "El nombre no puede superar los 100 caracteres."
    return True, ""


def validar_categoria(categoria: str) -> tuple[bool, str]:
    """Valida que la categoria pertenezca al conjunto de categorias permitidas."""
    if not isinstance(categoria, str):
        return False, "La categoria debe ser una cadena de texto."
    if categoria.strip().lower() not in CATEGORIAS_VALIDAS:
        return False, f"Categoria invalida. Opciones validas: {', '.join(sorted(CATEGORIAS_VALIDAS))}."
    return True, ""


def validar_marca_moto(marca: str) -> tuple[bool, str]:
    """Valida que la marca de moto pertenezca al conjunto de marcas permitidas."""
    if not isinstance(marca, str):
        return False, "La marca de moto debe ser una cadena de texto."
    if marca.strip().lower() not in MARCAS_MOTO_VALIDAS:
        return False, f"Marca invalida. Opciones validas: {', '.join(sorted(MARCAS_MOTO_VALIDAS))}."
    return True, ""


def validar_precio(precio: float | int | str) -> tuple[bool, str]:
    """Valida que el precio sea un numero positivo menor a 99,999,999."""
    try:
        precio = float(precio)
    except (ValueError, TypeError):
        return False, "El precio debe ser un numero."
    if precio <= 0:
        return False, "El precio debe ser mayor a 0."
    if precio > 99_999_999:
        return False, "El precio excede el valor maximo permitido."
    return True, ""


def validar_stock(stock: int | str) -> tuple[bool, str]:
    """Valida que el stock sea un entero no negativo."""
    try:
        stock = int(stock)
    except (ValueError, TypeError):
        return False, "El stock debe ser un numero entero."
    if stock < 0:
        return False, "El stock no puede ser negativo."
    return True, ""


def validar_repuesto(datos: dict) -> tuple[bool, list[str]]:
    """
    Valida todos los campos obligatorios de un repuesto.
    Retorna (True, []) si todo es valido, o (False, [errores]) si hay problemas.
    """
    errores: list[str] = []

    campos: dict[str, object] = {
        "codigo":     validar_codigo,
        "nombre":     validar_nombre,
        "categoria":  validar_categoria,
        "marca_moto": validar_marca_moto,
        "precio":     validar_precio,
        "stock":      validar_stock,
    }

    for campo, fn_validar in campos.items():
        if campo not in datos:
            errores.append(f"Campo obligatorio faltante: '{campo}'.")
            continue
        ok, mensaje = fn_validar(datos[campo])
        if not ok:
            errores.append(f"{campo}: {mensaje}")

    return len(errores) == 0, errores
