"""
service.py
Logica de negocio del inventario. Todas las operaciones CRUD pasan por aqui.
No contiene logica de presentacion ni de entrada de datos.
"""

from validate import validar_repuesto, validar_codigo
from file import load_data, save_data

CAMPOS_EDITABLES: set[str] = {"nombre", "categoria", "marca_moto", "precio", "stock", "descripcion"}
CAMPOS_ORDEN_VALIDOS: set[str] = {"codigo", "nombre", "categoria", "marca_moto", "precio", "stock"}


def _normalizar(datos: dict) -> dict:
    """Estandariza tipos y formato de texto antes de guardar un registro."""
    return {
        "codigo":      datos["codigo"].strip().upper(),
        "nombre":      datos["nombre"].strip(),
        "categoria":   datos["categoria"].strip().lower(),
        "marca_moto":  datos["marca_moto"].strip().lower(),
        "precio":      round(float(datos["precio"]), 2),
        "stock":       int(datos["stock"]),
        "descripcion": datos.get("descripcion", "").strip(),
    }


def new_register(datos: dict) -> tuple[bool, str]:
    """
    Crea un nuevo repuesto en el inventario.
    Retorna (True, mensaje) si se registro correctamente,
    o (False, mensaje) si hay errores de validacion o el codigo ya existe.
    """
    ok, errores = validar_repuesto(datos)
    if not ok:
        return False, "\n".join(errores)

    datos = _normalizar(datos)
    codigo = datos["codigo"]
    inventario = load_data()

    if codigo in inventario:
        return False, f"Ya existe un repuesto con el codigo '{codigo}'."

    inventario[codigo] = datos
    if not save_data(inventario):
        return False, f"El repuesto '{codigo}' se proceso pero no se pudo guardar en disco."

    return True, f"Repuesto '{codigo}' registrado correctamente."


def list_records(ordenar_por: str = "codigo") -> list[dict]:
    """
    Retorna todos los repuestos ordenados por el campo indicado.
    Si el campo no es valido, ordena por codigo.
    """
    inventario = load_data()

    if ordenar_por not in CAMPOS_ORDEN_VALIDOS:
        ordenar_por = "codigo"

    return sorted(inventario.values(), key=lambda r: r[ordenar_por])


def search_record(codigo: str) -> tuple[bool, dict | str]:
    """
    Busca un repuesto por su codigo exacto.
    Retorna (True, dict) si lo encuentra o (False, mensaje) si no existe o el codigo es invalido.
    """
    ok, mensaje = validar_codigo(codigo)
    if not ok:
        return False, f"Codigo invalido: {mensaje}"

    inventario = load_data()
    codigo = codigo.strip().upper()

    if codigo not in inventario:
        return False, f"No se encontro ningun repuesto con el codigo '{codigo}'."

    return True, inventario[codigo]


def filter_records(
    categoria: str = "",
    marca_moto: str = "",
    nombre: str = "",
    ordenar_por: str = "codigo",
) -> list[dict]:
    """
    Filtra el inventario por categoria, marca y/o nombre parcial.
    Los parametros vacios se ignoran. Retorna lista ordenada.
    """
    inventario = load_data()

    resultados = [
        r for r in inventario.values()
        if (not categoria  or r["categoria"]  == categoria.strip().lower())
        and (not marca_moto or r["marca_moto"] == marca_moto.strip().lower())
        and (not nombre    or nombre.strip().lower() in r["nombre"].lower())
    ]

    if ordenar_por not in CAMPOS_ORDEN_VALIDOS:
        ordenar_por = "codigo"

    return sorted(resultados, key=lambda r: r[ordenar_por])


def update_record(codigo: str, cambios: dict) -> tuple[bool, str]:
    """
    Actualiza los campos indicados de un repuesto existente.
    Solo se permiten los campos definidos en CAMPOS_EDITABLES.
    Retorna (True, mensaje) o (False, mensaje) segun el resultado.
    """
    ok, mensaje = validar_codigo(codigo)
    if not ok:
        return False, f"Codigo invalido: {mensaje}"

    codigo = codigo.strip().upper()
    inventario = load_data()

    if codigo not in inventario:
        return False, f"No se encontro ningun repuesto con el codigo '{codigo}'."

    if not cambios:
        return False, "No se enviaron campos para actualizar."

    campos_invalidos = [c for c in cambios if c not in CAMPOS_EDITABLES]
    if campos_invalidos:
        return False, f"Campos no permitidos: {', '.join(campos_invalidos)}."

    registro_actualizado = {**inventario[codigo], **cambios}

    ok, errores = validar_repuesto(registro_actualizado)
    if not ok:
        return False, "\n".join(errores)

    inventario[codigo] = _normalizar(registro_actualizado)

    if not save_data(inventario):
        return False, "Los cambios se procesaron pero no se pudieron guardar en disco."

    return True, f"Repuesto '{codigo}' actualizado correctamente."


def delete_record(codigo: str) -> tuple[bool, str]:
    """
    Elimina un repuesto del inventario por su codigo.
    Retorna (True, mensaje) o (False, mensaje) segun el resultado.
    """
    ok, mensaje = validar_codigo(codigo)
    if not ok:
        return False, f"Codigo invalido: {mensaje}"

    codigo = codigo.strip().upper()
    inventario = load_data()

    if codigo not in inventario:
        return False, f"No se encontro ningun repuesto con el codigo '{codigo}'."

    del inventario[codigo]

    if not save_data(inventario):
        return False, f"El repuesto '{codigo}' se elimino en memoria pero no se pudo guardar en disco."

    return True, f"Repuesto '{codigo}' eliminado correctamente."
