# Inventario de Repuestos para Motos

Sistema de gestión de inventario por consola, desarrollado en Python.

## Requisitos

- Python 3.10 o superior

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Estructura del proyecto

```
├── validate.py       # Validaciones de campos
├── file.py           # Lectura y escritura en JSON
├── service.py        # Lógica de negocio (CRUD)
├── integration.py    # Generación de registros falsos con faker
├── menu.py           # Menú interactivo en consola
├── main.py           # Punto de entrada
├── requirements.txt  # Dependencias
└── data/
    └── registros.json
```

## Opciones del menú

| # | Opción                  | Descripción                                      |
|---|-------------------------|--------------------------------------------------|
| 1 | Crear repuesto          | Registra un repuesto nuevo con validación        |
| 2 | Listar inventario       | Muestra todos los repuestos con orden a elegir   |
| 3 | Buscar por codigo       | Búsqueda exacta por código                       |
| 4 | Filtrar repuestos       | Filtra por categoría, marca y/o nombre parcial   |
| 5 | Actualizar repuesto     | Edita campos de un repuesto existente            |
| 6 | Eliminar repuesto       | Elimina un repuesto con confirmación             |
| 7 | Generar registros falsos| Crea N registros de prueba con faker             |
| 8 | Salir                   |                                                  |

## Categorías válidas

`motor` `frenos` `suspension` `electrico` `transmision` `carroceria` `filtros` `lubricacion`

## Marcas válidas

`honda` `yamaha` `suzuki` `kawasaki` `bajaj` `tvs` `ktm` `hero` `generica`
