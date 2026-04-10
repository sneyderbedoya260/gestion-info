# Inventario de Repuestos para Motos

Sistema de gestion de inventario por consola, desarrollado en Python.

## Requisitos

- Python 3.10 o superior

## Instalacion

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Ejecutar pruebas

Con unittest (sin dependencias adicionales):

```bash
python -m unittest discover -s tests -v
```

Con pytest (requiere `pip install pytest`):

```bash
pytest tests/ -v
```

## Estructura del proyecto

```
├── validate.py         Validaciones de campos
├── file.py             Lectura y escritura en JSON
├── service.py          Logica de negocio (CRUD)
├── integration.py      Generacion de registros falsos con faker
├── menu.py             Menu interactivo en consola
├── main.py             Punto de entrada
├── requirements.txt    Dependencias
├── tests/
│   ├── test_validate.py    Pruebas unitarias de validaciones
│   └── test_service.py     Pruebas de integracion del CRUD
└── data/
    └── registros.json
```

## Opciones del menu

| # | Opcion                  | Descripcion                                     |
|---|-------------------------|-------------------------------------------------|
| 1 | Crear repuesto          | Registra un repuesto nuevo con validacion       |
| 2 | Listar inventario       | Muestra todos los repuestos con orden a elegir  |
| 3 | Buscar por codigo       | Busqueda exacta por codigo                      |
| 4 | Filtrar repuestos       | Filtra por categoria, marca y/o nombre parcial  |
| 5 | Actualizar repuesto     | Edita campos de un repuesto existente           |
| 6 | Eliminar repuesto       | Elimina un repuesto con confirmacion            |
| 7 | Generar registros falsos| Crea N registros de prueba con faker            |
| 8 | Salir                   |                                                 |

## Categorias validas

`motor` `frenos` `suspension` `electrico` `transmision` `carroceria` `filtros` `lubricacion`

## Marcas validas

`honda` `yamaha` `suzuki` `kawasaki` `bajaj` `tvs` `ktm` `hero` `generica`
