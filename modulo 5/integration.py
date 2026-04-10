import random
import string
from faker import Faker
from service import new_register

fake = Faker("es_MX")

CATEGORIAS = [
    "motor", "frenos", "suspension", "electrico",
    "transmision", "carroceria", "filtros", "lubricacion",
]

MARCAS = [
    "honda", "yamaha", "suzuki", "kawasaki",
    "bajaj", "tvs", "ktm", "hero", "generica",
]

NOMBRES_POR_CATEGORIA = {
    "motor":       ["Piston", "Cigüeñal", "Culata", "Junta de motor", "Valvula de escape"],
    "frenos":      ["Pastilla delantera", "Pastilla trasera", "Disco de freno", "Cable de freno", "Bomba de freno"],
    "suspension":  ["Amortiguador trasero", "Horquilla delantera", "Resorte de suspension", "Buje delantero"],
    "electrico":   ["Regulador de voltaje", "Bobina de encendido", "CDI", "Interruptor de arranque", "Bateria"],
    "transmision": ["Kit de arrastre", "Clutch", "Piñon de salida", "Corona", "Cable de cambios"],
    "carroceria":  ["Carenado lateral", "Guardabarro", "Manillar", "Espejo retrovisor", "Asiento"],
    "filtros":     ["Filtro de aire", "Filtro de aceite", "Filtro de combustible"],
    "lubricacion": ["Aceite de motor", "Grasa de cadena", "Liquido de frenos"],
}


def _generar_codigo(*prefijos, longitud: int = 3) -> str:
    prefijo = prefijos[0] if prefijos else "REP"
    sufijo = "".join(random.choices(string.digits, k=longitud))
    return f"{prefijo}{sufijo}"


def _construir_repuesto(**campos) -> dict:
    categoria = campos.get("categoria", random.choice(CATEGORIAS))
    nombre_base = random.choice(NOMBRES_POR_CATEGORIA[categoria])
    marca = campos.get("marca_moto", random.choice(MARCAS))

    return {
        "codigo":      campos.get("codigo", _generar_codigo(categoria[:3].upper())),
        "nombre":      campos.get("nombre", f"{nombre_base} {marca.capitalize()}"),
        "categoria":   categoria,
        "marca_moto":  marca,
        "precio":      campos.get("precio", round(random.uniform(8000, 350000), 2)),
        "stock":       campos.get("stock", random.randint(1, 30)),
        "descripcion": campos.get("descripcion", fake.sentence(nb_words=6)),
    }


def generar_registros_falsos(*categorias_filtro, cantidad: int = 10, **campos_fijos) -> dict:
    generados = 0
    omitidos = 0
    errores = []

    pool_categorias = list(categorias_filtro) if categorias_filtro else CATEGORIAS

    for _ in range(cantidad):
        campos = {**campos_fijos, "categoria": random.choice(pool_categorias)}
        datos = _construir_repuesto(**campos)

        exito, mensaje = new_register(datos)
        if exito:
            generados += 1
        else:
            if "Ya existe" in mensaje:
                omitidos += 1
            else:
                errores.append(mensaje)

    return {
        "generados": generados,
        "omitidos":  omitidos,
        "errores":   errores,
    }
