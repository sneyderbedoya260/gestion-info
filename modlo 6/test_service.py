"""
tests/test_service.py
Pruebas de integracion para las operaciones CRUD de service.py.
Usa un archivo JSON temporal para no tocar el inventario real.
"""

import unittest
import sys
import os
import json
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import file as file_module


def _repuesto_base(**overrides) -> dict:
    datos = {
        "codigo":     "TST001",
        "nombre":     "Repuesto de prueba",
        "categoria":  "filtros",
        "marca_moto": "honda",
        "precio":     50000,
        "stock":      5,
    }
    datos.update(overrides)
    return datos


class TestCRUD(unittest.TestCase):

    def setUp(self):
        """Redirige RUTA_DATOS a un archivo temporal antes de cada prueba."""
        self.tmp_dir = tempfile.mkdtemp()
        self.ruta_original = file_module.RUTA_DATOS
        file_module.RUTA_DATOS = os.path.join(self.tmp_dir, "test_registros.json")

        from service import new_register, list_records, search_record, update_record, delete_record
        self.new_register  = new_register
        self.list_records  = list_records
        self.search_record = search_record
        self.update_record = update_record
        self.delete_record = delete_record

    def tearDown(self):
        """Restaura RUTA_DATOS y elimina el archivo temporal."""
        file_module.RUTA_DATOS = self.ruta_original
        tmp_json = os.path.join(self.tmp_dir, "test_registros.json")
        if os.path.exists(tmp_json):
            os.remove(tmp_json)
        os.rmdir(self.tmp_dir)

    # ── CREATE ────────────────────────────────────────

    def test_crear_repuesto_valido(self):
        ok, msg = self.new_register(_repuesto_base())
        self.assertTrue(ok)
        self.assertIn("TST001", msg)

    def test_crear_repuesto_duplicado(self):
        self.new_register(_repuesto_base())
        ok, msg = self.new_register(_repuesto_base())
        self.assertFalse(ok)
        self.assertIn("Ya existe", msg)

    def test_crear_repuesto_campos_invalidos(self):
        ok, msg = self.new_register(_repuesto_base(precio=-100, codigo="XX"))
        self.assertFalse(ok)

    # ── READ ──────────────────────────────────────────

    def test_listar_retorna_lista(self):
        self.new_register(_repuesto_base())
        registros = self.list_records()
        self.assertIsInstance(registros, list)
        self.assertEqual(len(registros), 1)

    def test_listar_orden_por_precio(self):
        self.new_register(_repuesto_base(codigo="TST001", precio=80000))
        self.new_register(_repuesto_base(codigo="TST002", precio=20000))
        registros = self.list_records(ordenar_por="precio")
        self.assertLessEqual(registros[0]["precio"], registros[1]["precio"])

    def test_buscar_codigo_existente(self):
        self.new_register(_repuesto_base())
        ok, resultado = self.search_record("TST001")
        self.assertTrue(ok)
        self.assertEqual(resultado["codigo"], "TST001")

    def test_buscar_codigo_inexistente(self):
        ok, msg = self.search_record("ZZZ999")
        self.assertFalse(ok)
        self.assertIn("No se encontro", msg)

    def test_buscar_codigo_invalido(self):
        ok, msg = self.search_record("XY")
        self.assertFalse(ok)
        self.assertIn("invalido", msg.lower())

    # ── UPDATE ────────────────────────────────────────

    def test_actualizar_campo_valido(self):
        self.new_register(_repuesto_base())
        ok, msg = self.update_record("TST001", {"stock": 99})
        self.assertTrue(ok)
        _, r = self.search_record("TST001")
        self.assertEqual(r["stock"], 99)

    def test_actualizar_campo_no_permitido(self):
        self.new_register(_repuesto_base())
        ok, msg = self.update_record("TST001", {"codigo": "OTRO1"})
        self.assertFalse(ok)
        self.assertIn("no permitidos", msg.lower())

    def test_actualizar_con_valor_invalido(self):
        self.new_register(_repuesto_base())
        ok, _ = self.update_record("TST001", {"precio": -500})
        self.assertFalse(ok)

    def test_actualizar_registro_inexistente(self):
        ok, msg = self.update_record("ZZZ999", {"stock": 1})
        self.assertFalse(ok)
        self.assertIn("No se encontro", msg)

    # ── DELETE ────────────────────────────────────────

    def test_eliminar_registro_existente(self):
        self.new_register(_repuesto_base())
        ok, msg = self.delete_record("TST001")
        self.assertTrue(ok)
        self.assertEqual(len(self.list_records()), 0)

    def test_eliminar_registro_inexistente(self):
        ok, msg = self.delete_record("ZZZ999")
        self.assertFalse(ok)
        self.assertIn("No se encontro", msg)

    # ── PERSISTENCIA ─────────────────────────────────

    def test_datos_persisten_en_disco(self):
        self.new_register(_repuesto_base())
        with open(file_module.RUTA_DATOS, "r", encoding="utf-8") as f:
            contenido = json.load(f)
        self.assertIn("TST001", contenido)


if __name__ == "__main__":
    unittest.main()
