"""
file.py
Lectura y escritura del inventario en disco usando JSON.
Toda operacion de I/O del proyecto pasa por este modulo.
"""

import json
import os

RUTA_DATOS: str = os.path.join("data", "registros.json")


def _garantizar_directorio() -> None:
    """Crea el directorio de datos si no existe."""
    os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)


def load_data() -> dict:
    """
    Carga el inventario desde el archivo JSON.
    Retorna un dict vacio si el archivo no existe o esta corrupto.
    """
    _garantizar_directorio()

    if not os.path.exists(RUTA_DATOS):
        return {}

    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                return {}
            return json.loads(contenido)
    except json.JSONDecodeError as e:
        print(f"[ERROR] El archivo '{RUTA_DATOS}' tiene formato invalido: {e}")
        return {}
    except PermissionError:
        print(f"[ERROR] Sin permisos para leer '{RUTA_DATOS}'.")
        return {}
    except OSError as e:
        print(f"[ERROR] No se pudo leer '{RUTA_DATOS}': {e}")
        return {}


def save_data(data: dict) -> bool:
    """
    Guarda el inventario en disco de forma atomica usando un archivo temporal.
    Retorna True si tuvo exito, False si hubo un error de escritura.
    """
    _garantizar_directorio()

    ruta_tmp = RUTA_DATOS + ".tmp"

    try:
        with open(ruta_tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(ruta_tmp, RUTA_DATOS)
        return True
    except PermissionError:
        print(f"[ERROR] Sin permisos para escribir en '{RUTA_DATOS}'.")
        return False
    except OSError as e:
        print(f"[ERROR] No se pudo guardar '{RUTA_DATOS}': {e}")
        return False
    finally:
        if os.path.exists(ruta_tmp):
            try:
                os.remove(ruta_tmp)
            except OSError:
                pass
