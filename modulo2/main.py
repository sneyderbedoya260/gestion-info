from service import crear_repuesto, listar_repuestos, total_repuestos


def imprimir_repuesto(r: dict) -> None:
    print(f"  [{r['codigo']}] {r['nombre']}")
    print(f"    Categoria : {r['categoria']}")
    print(f"    Marca moto: {r['marca_moto']}")
    print(f"    Precio    : ${r['precio']:,.2f}")
    print(f"    Stock     : {r['stock']} unidades")
    if r["descripcion"]:
        print(f"    Descripcion: {r['descripcion']}")
    print()


def main():
    repuestos_nuevos = [
        {
            "codigo": "FLT001",
            "nombre": "Filtro de aire CB190",
            "categoria": "filtros",
            "marca_moto": "honda",
            "precio": 35000,
            "stock": 12,
            "descripcion": "Compatible con modelos CB190R y CB190X",
        },
        {
            "codigo": "FRN002",
            "nombre": "Pastilla de freno delantera",
            "categoria": "frenos",
            "marca_moto": "yamaha",
            "precio": 48500,
            "stock": 8,
        },
        {
            "codigo": "MTR003",
            "nombre": "Kit de arrastre",
            "categoria": "transmision",
            "marca_moto": "bajaj",
            "precio": 120000,
            "stock": 5,
            "descripcion": "Cadena + corona + pinon",
        },
        {
            "codigo": "ELC004",
            "nombre": "Regulador de voltaje",
            "categoria": "electrico",
            "marca_moto": "honda",
            "precio": 75000,
            "stock": 3,
        },
        {
            "codigo": "SUS005",
            "nombre": "Amortiguador trasero",
            "categoria": "suspension",
            "marca_moto": "yamaha",
            "precio": 210000,
            "stock": 2,
            "descripcion": "Repuesto original de fabrica",
        },
        # Duplicado — debe fallar
        {
            "codigo": "FLT001",
            "nombre": "Filtro duplicado",
            "categoria": "filtros",
            "marca_moto": "honda",
            "precio": 10000,
            "stock": 1,
        },
        # Datos invalidos — debe fallar
        {
            "codigo": "XX",
            "nombre": "A",
            "categoria": "inexistente",
            "marca_moto": "honda",
            "precio": -500,
            "stock": "no es numero",
        },
    ]

    print("=" * 50)
    print("CARGA DE REPUESTOS")
    print("=" * 50)

    for datos in repuestos_nuevos:
        ok, mensaje = crear_repuesto(datos)
        estado = "OK" if ok else "ERROR"
        print(f"[{estado}] {mensaje}")

    print()
    print("=" * 50)
    print(f"INVENTARIO ACTUAL  ({total_repuestos()} repuestos)")
    print("=" * 50)

    repuestos = listar_repuestos()
    if not repuestos:
        print("No hay repuestos registrados.")
    else:
        for r in repuestos:
            imprimir_repuesto(r)


if __name__ == "__main__":
    main()
