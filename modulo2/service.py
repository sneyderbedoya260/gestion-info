from validate import validar_repuesto
from file import load_data, save_data


def _normalizar(datos: dict) -> dict:
    return {
        "codigo": datos["codigo"].strip().upper(),
        "nombre": datos["nombre"].strip(),
        "categoria": datos["categoria"].strip().lower(),
        "marca_moto": datos["marca_moto"].strip().lower(),
        "precio": round(float(datos["precio"]), 2),
        "stock": int(datos["stock"]),
        "descripcion": datos.get("descripcion", "").strip(),
    }


def crear_repuesto(datos: dict) -> tuple[bool, str]:
    ok, errores = validar_repuesto(datos)
    if not ok:
        return False, "\n".join(errores)

    datos = _normalizar(datos)
    codigo = datos["codigo"]

    inventario = load_data()

    if codigo in inventario:
        return False, f"Ya existe un repuesto con el codigo '{codigo}'."

    inventario[codigo] = datos
    guardado = save_data(inventario)

    if not guardado:
        return False, f"El repuesto '{codigo}' se proceso pero no se pudo guardar en disco."

    return True, f"Repuesto '{codigo}' registrado correctamente."


def listar_repuestos() -> list[dict]:
    return list(load_data().values())


def buscar_por_codigo(codigo: str) -> dict | None:
    return load_data().get(codigo.strip().upper())


def total_repuestos() -> int:
    return len(load_data())
