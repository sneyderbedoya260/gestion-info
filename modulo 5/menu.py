from colorama import init, Fore, Style
from service import (
    new_register,
    list_records,
    search_record,
    filter_records,
    update_record,
    delete_record,
)
from integration import generar_registros_falsos, CATEGORIAS

init(autoreset=True)

# ── Helpers de impresion ──────────────────────────────────────────────────────

def ok(msg: str) -> None:
    print(Fore.GREEN + f"[OK] {msg}")

def error(msg: str) -> None:
    print(Fore.RED + f"[ERROR] {msg}")

def info(msg: str) -> None:
    print(Fore.CYAN + msg)

def advertencia(msg: str) -> None:
    print(Fore.YELLOW + msg)

def separador() -> None:
    print(Fore.WHITE + Style.DIM + "─" * 50)


def imprimir_repuesto(r: dict) -> None:
    print(
        Fore.CYAN + f"  [{r['codigo']}] " +
        Fore.WHITE + r["nombre"]
    )
    print(f"    Categoria : {r['categoria']}")
    print(f"    Marca moto: {r['marca_moto']}")
    print(Fore.GREEN + f"    Precio    : ${r['precio']:,.2f}")
    stock_color = Fore.RED if r["stock"] == 0 else Fore.YELLOW if r["stock"] <= 3 else Fore.WHITE
    print(stock_color + f"    Stock     : {r['stock']} unidades")
    if r["descripcion"]:
        print(Fore.WHITE + Style.DIM + f"    Descripcion: {r['descripcion']}")
    print()


def pedir_texto(campo: str, obligatorio: bool = True) -> str:
    while True:
        valor = input(f"  {campo}: ").strip()
        if valor:
            return valor
        if not obligatorio:
            return ""
        advertencia(f"  El campo '{campo}' es obligatorio.")


def pedir_numero(campo: str, tipo: type = float) -> float | int | None:
    while True:
        entrada = input(f"  {campo}: ").strip()
        if not entrada:
            return None
        try:
            return tipo(entrada)
        except ValueError:
            advertencia(f"  Ingresa un valor numerico valido.")


def pedir_opcion(opciones: list[str]) -> str:
    while True:
        try:
            entrada = int(input(Fore.YELLOW + "\n  Opcion: " + Style.RESET_ALL).strip())
            if 1 <= entrada <= len(opciones):
                return opciones[entrada - 1]
            advertencia(f"  Elige una opcion entre 1 y {len(opciones)}.")
        except ValueError:
            advertencia("  Ingresa un numero, no texto.")


# ── Flujos del CRUD ───────────────────────────────────────────────────────────

def flujo_crear() -> None:
    separador()
    info("NUEVO REPUESTO")
    separador()

    datos = {
        "codigo":     pedir_texto("Codigo (ej: FLT001)"),
        "nombre":     pedir_texto("Nombre"),
        "categoria":  pedir_texto("Categoria (motor/frenos/suspension/electrico/transmision/carroceria/filtros/lubricacion)"),
        "marca_moto": pedir_texto("Marca de moto"),
        "precio":     pedir_numero("Precio", float) or 0,
        "stock":      pedir_numero("Stock", int) or 0,
        "descripcion": pedir_texto("Descripcion (Enter para omitir)", obligatorio=False),
    }

    exito, mensaje = new_register(datos)
    print()
    ok(mensaje) if exito else error(mensaje)


def flujo_listar() -> None:
    separador()
    info("LISTAR INVENTARIO")
    separador()

    print("  Ordenar por:")
    print("  1. Codigo")
    print("  2. Nombre")
    print("  3. Precio")
    print("  4. Stock")
    print("  5. Categoria")

    campos = ["codigo", "nombre", "precio", "stock", "categoria"]
    campo = pedir_opcion(campos)

    registros = list_records(ordenar_por=campo)
    print()

    if not registros:
        advertencia("  No hay repuestos registrados.")
        return

    separador()
    info(f"  {len(registros)} repuesto(s) — ordenado por {campo}")
    separador()
    for r in registros:
        imprimir_repuesto(r)


def flujo_buscar() -> None:
    separador()
    info("BUSCAR POR CODIGO")
    separador()

    codigo = pedir_texto("Codigo")
    exito, resultado = search_record(codigo)
    print()

    if exito:
        imprimir_repuesto(resultado)
    else:
        error(resultado)


def flujo_filtrar() -> None:
    separador()
    info("FILTRAR REPUESTOS")
    separador()
    advertencia("  Deja en blanco para omitir un filtro.")
    print()

    categoria  = pedir_texto("Categoria", obligatorio=False)
    marca_moto = pedir_texto("Marca de moto", obligatorio=False)
    nombre     = pedir_texto("Nombre (busqueda parcial)", obligatorio=False)

    resultados = filter_records(
        categoria=categoria,
        marca_moto=marca_moto,
        nombre=nombre,
    )
    print()

    if not resultados:
        advertencia("  No se encontraron repuestos con esos filtros.")
        return

    separador()
    info(f"  {len(resultados)} resultado(s)")
    separador()
    for r in resultados:
        imprimir_repuesto(r)


def flujo_actualizar() -> None:
    separador()
    info("ACTUALIZAR REPUESTO")
    separador()

    codigo = pedir_texto("Codigo del repuesto a editar")
    exito, resultado = search_record(codigo)

    if not exito:
        print()
        error(resultado)
        return

    print()
    info("  Registro actual:")
    imprimir_repuesto(resultado)
    advertencia("  Ingresa los nuevos valores (Enter para conservar el actual).\n")

    cambios = {}

    nombre = pedir_texto(f"  Nombre [{resultado['nombre']}]", obligatorio=False)
    if nombre:
        cambios["nombre"] = nombre

    categoria = pedir_texto(f"  Categoria [{resultado['categoria']}]", obligatorio=False)
    if categoria:
        cambios["categoria"] = categoria

    marca = pedir_texto(f"  Marca moto [{resultado['marca_moto']}]", obligatorio=False)
    if marca:
        cambios["marca_moto"] = marca

    precio_str = input(f"  Precio [{resultado['precio']}]: ").strip()
    if precio_str:
        try:
            cambios["precio"] = float(precio_str)
        except ValueError:
            advertencia("  Precio invalido, se conserva el actual.")

    stock_str = input(f"  Stock [{resultado['stock']}]: ").strip()
    if stock_str:
        try:
            cambios["stock"] = int(stock_str)
        except ValueError:
            advertencia("  Stock invalido, se conserva el actual.")

    descripcion = pedir_texto(f"  Descripcion [{resultado['descripcion'] or 'sin descripcion'}]", obligatorio=False)
    if descripcion:
        cambios["descripcion"] = descripcion

    if not cambios:
        advertencia("\n  No se realizo ningun cambio.")
        return

    exito, mensaje = update_record(codigo, cambios)
    print()
    ok(mensaje) if exito else error(mensaje)


def flujo_eliminar() -> None:
    separador()
    info("ELIMINAR REPUESTO")
    separador()

    codigo = pedir_texto("Codigo del repuesto a eliminar")
    exito, resultado = search_record(codigo)

    if not exito:
        print()
        error(resultado)
        return

    print()
    info("  Repuesto a eliminar:")
    imprimir_repuesto(resultado)

    confirmar = input(Fore.RED + f"  Confirmar eliminacion de '{codigo.upper()}' (s/n): " + Style.RESET_ALL).strip().lower()

    if confirmar != "s":
        advertencia("\n  Eliminacion cancelada.")
        return

    exito, mensaje = delete_record(codigo)
    print()
    ok(mensaje) if exito else error(mensaje)


def flujo_generar_falsos() -> None:
    separador()
    info("GENERAR REGISTROS FALSOS")
    separador()

    cantidad_str = input("  Cantidad a generar (Enter para 10): ").strip()
    try:
        cantidad = int(cantidad_str) if cantidad_str else 10
        if cantidad < 1 or cantidad > 100:
            advertencia("  Valor fuera de rango, se usara 10.")
            cantidad = 10
    except ValueError:
        advertencia("  Valor invalido, se usara 10.")
        cantidad = 10

    print()
    print(f"  Categorias disponibles: {', '.join(sorted(CATEGORIAS))}")
    cats_str = input("  Filtrar por categorias (separadas por coma, Enter para todas): ").strip()

    categorias_filtro = []
    if cats_str:
        categorias_filtro = [c.strip().lower() for c in cats_str.split(",") if c.strip()]

    marca_fija = input("  Fijar marca de moto (Enter para aleatoria): ").strip().lower()

    campos_fijos = {}
    if marca_fija:
        campos_fijos["marca_moto"] = marca_fija

    print()
    advertencia(f"  Generando {cantidad} repuesto(s)...")

    resultado = generar_registros_falsos(
        *categorias_filtro,
        cantidad=cantidad,
        **campos_fijos,
    )

    print()
    ok(f"Registros creados    : {resultado['generados']}")
    if resultado["omitidos"]:
        advertencia(f"  Omitidos (duplicados): {resultado['omitidos']}")
    if resultado["errores"]:
        for e in resultado["errores"]:
            error(e)


# ── Menu principal ────────────────────────────────────────────────────────────

OPCIONES = [
    ("1", "Crear repuesto",           flujo_crear),
    ("2", "Listar inventario",        flujo_listar),
    ("3", "Buscar por codigo",        flujo_buscar),
    ("4", "Filtrar repuestos",        flujo_filtrar),
    ("5", "Actualizar repuesto",      flujo_actualizar),
    ("6", "Eliminar repuesto",        flujo_eliminar),
    ("7", "Generar registros falsos", flujo_generar_falsos),
    ("8", "Salir",                    None),
]


def mostrar_menu() -> None:
    print()
    print(Fore.CYAN + Style.BRIGHT + "  INVENTARIO DE REPUESTOS PARA MOTOS")
    separador()
    for num, etiqueta, _ in OPCIONES:
        color = Fore.RED if num == "8" else Fore.MAGENTA if num == "7" else Fore.WHITE
        print(color + f"  {num}. {etiqueta}")
    separador()


def ejecutar_menu() -> None:
    while True:
        mostrar_menu()

        try:
            entrada = int(input(Fore.YELLOW + "  Opcion: " + Style.RESET_ALL).strip())
        except ValueError:
            print()
            advertencia("  Ingresa un numero entre 1 y 8.")
            continue

        if entrada < 1 or entrada > len(OPCIONES):
            print()
            advertencia(f"  Opcion invalida. Elige entre 1 y {len(OPCIONES)}.")
            continue

        _, etiqueta, accion = OPCIONES[entrada - 1]

        if accion is None:
            print()
            info("  Hasta luego.")
            print()
            break

        print()
        accion()
        input(Fore.WHITE + Style.DIM + "\n  Presiona Enter para continuar...")
