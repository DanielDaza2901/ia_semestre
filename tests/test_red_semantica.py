"""
Pruebas Unitarias de la Red Semántica - Semana 14
Autor: Daniel Eduardo Daza Cuello (ETITC - Ingeniería de Sistemas)
"""

import unittest
from semana14_red_semantica import RedSemantica, normalizar

class TestRedSemantica(unittest.TestCase):

    def setUp(self):
        self.red = RedSemantica()
        self.red.procesar_oracion("Un firewall es un dispositivo de red")
        self.red.procesar_oracion("Un dispositivo de red es un activo de ti")
        self.red.procesar_oracion("Un activo de ti requiere conexion segura")

    def test_normalizacion(self):
        self.assertEqual(normalizar("  Conexión  Segura  "), "conexion_segura")
        self.assertEqual(normalizar("Servidor MÁXIMO"), "servidor_maximo")

    def test_relaciones_explicitas(self):
        self.assertIn(("firewall", "es_un", "dispositivo_red"), self.red.triples)

    def test_inferencia_transitividad(self):
        self.assertTrue(self.red.es_un("firewall", "activo_ti"))

    def test_herencia_propiedades(self):
        propiedades = self.red.consultar_propiedades("firewall")
        self.assertIn("conexion_segura", propiedades)

    def test_consulta_sin_evidencia(self):
        self.assertFalse(self.red.es_un("firewall", "servidor"))

    def test_oracion_invalida_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.red.procesar_oracion("Frase gramatical no soportada por el sistema")

if __name__ == "__main__":
    unittest.main()