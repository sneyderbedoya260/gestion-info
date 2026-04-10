"""
tests/test_validate.py
Pruebas unitarias para las funciones de validacion.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from validate import (
    validar_codigo,
    validar_nombre,
    validar_categoria,
    validar_marca_moto,
    validar_precio,
    validar_stock,
    validar_repuesto,
)


class TestValidarCodigo(unittest.TestCase):

    def test_codigo_valido(self):
        ok, _ = validar_codigo("FLT001")
        self.assertTrue(ok)

    def test_codigo_muy_corto(self):
        ok, msg = validar_codigo("AB")
        self.assertFalse(ok)
        self.assertIn("4 y 20", msg)

    def test_codigo_con_espacios(self):
        ok, _ = validar_codigo("FLT 01")
        self.assertFalse(ok)

    def test_codigo_con_simbolos(self):
        ok, _ = validar_codigo("FLT-01")
        self.assertFalse(ok)

    def test_codigo_no_string(self):
        ok, _ = validar_codigo(1234)
        self.assertFalse(ok)


class TestValidarNombre(unittest.TestCase):

    def test_nombre_valido(self):
        ok, _ = validar_nombre("Filtro de aire")
        self.assertTrue(ok)

    def test_nombre_muy_corto(self):
        ok, _ = validar_nombre("AB")
        self.assertFalse(ok)

    def test_nombre_muy_largo(self):
        ok, _ = validar_nombre("A" * 101)
        self.assertFalse(ok)


class TestValidarCategoria(unittest.TestCase):

    def test_categoria_valida(self):
        ok, _ = validar_categoria("filtros")
        self.assertTrue(ok)

    def test_categoria_valida_mayusculas(self):
        ok, _ = validar_categoria("FRENOS")
        self.assertTrue(ok)

    def test_categoria_invalida(self):
        ok, msg = validar_categoria("repuestos")
        self.assertFalse(ok)
        self.assertIn("Categoria invalida", msg)


class TestValidarPrecio(unittest.TestCase):

    def test_precio_valido(self):
        ok, _ = validar_precio(35000)
        self.assertTrue(ok)

    def test_precio_cero(self):
        ok, _ = validar_precio(0)
        self.assertFalse(ok)

    def test_precio_negativo(self):
        ok, _ = validar_precio(-100)
        self.assertFalse(ok)

    def test_precio_texto(self):
        ok, _ = validar_precio("no es numero")
        self.assertFalse(ok)

    def test_precio_excede_maximo(self):
        ok, _ = validar_precio(100_000_000)
        self.assertFalse(ok)


class TestValidarStock(unittest.TestCase):

    def test_stock_valido(self):
        ok, _ = validar_stock(10)
        self.assertTrue(ok)

    def test_stock_cero_es_valido(self):
        ok, _ = validar_stock(0)
        self.assertTrue(ok)

    def test_stock_negativo(self):
        ok, _ = validar_stock(-1)
        self.assertFalse(ok)

    def test_stock_texto(self):
        ok, _ = validar_stock("mucho")
        self.assertFalse(ok)


class TestValidarRepuesto(unittest.TestCase):

    def _repuesto_valido(self) -> dict:
        return {
            "codigo":     "FLT001",
            "nombre":     "Filtro de aire",
            "categoria":  "filtros",
            "marca_moto": "honda",
            "precio":     35000,
            "stock":      10,
        }

    def test_repuesto_completo_valido(self):
        ok, errores = validar_repuesto(self._repuesto_valido())
        self.assertTrue(ok)
        self.assertEqual(errores, [])

    def test_repuesto_campo_faltante(self):
        datos = self._repuesto_valido()
        del datos["precio"]
        ok, errores = validar_repuesto(datos)
        self.assertFalse(ok)
        self.assertTrue(any("precio" in e for e in errores))

    def test_repuesto_multiples_errores(self):
        ok, errores = validar_repuesto({
            "codigo":     "XX",
            "nombre":     "A",
            "categoria":  "inexistente",
            "marca_moto": "honda",
            "precio":     -1,
            "stock":      5,
        })
        self.assertFalse(ok)
        self.assertGreaterEqual(len(errores), 3)


if __name__ == "__main__":
    unittest.main()
