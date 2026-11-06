"""
Pruebas Unitarias del Motor de Inferencia - Semana 13
Autor: Daniel Eduardo Daza Cuello (ETITC - Ingeniería de Sistemas)
"""

import unittest
from src.semana13_motor_inferencia import Regla, inferir, REGLAS_PROYECTO

class TestMotorInferencia(unittest.TestCase):

    def test_caso_a_conclusion_demostrada(self):
        """Caso A: Verificar que con todas las evidencias se alcanza la conclusión final."""
        hechos_iniciales = {
            "alta_latencia_red", 
            "fallo_autenticacion_api", 
            "firewall_activo", 
            "canal_notificacion_operativo"
        }
        hechos_finales, traza = inferir(hechos_iniciales, REGLAS_PROYECTO)
        
        self.assertIn("alerta_incidente_despachada", hechos_finales)
        self.assertEqual(traza, ["R1_AlertaCritica", "R2_ProtocoloDefensiva", "R3_NotificacionAutomatica"])

    def test_caso_b_conclusion_no_demostrada(self):
        """Caso B: Verificar que al faltar una evidencia clave, la conclusión final no se alcanza."""
        hechos_iniciales = {
            "alta_latencia_red", 
            "fallo_autenticacion_api", 
            "firewall_activo"
            # Omitimos canal de notificación
        }
        hechos_finales, traza = inferir(hechos_iniciales, REGLAS_PROYECTO)
        
        self.assertNotIn("alerta_incidente_despachada", hechos_finales)
        # Se alcanzan conclusiones intermedias pero no la final
        self.assertIn("amenaza_seguridad_detectada", hechos_finales)
        self.assertIn("aislamiento_segmento_requerido", hechos_finales)
        self.assertEqual(traza, ["R1_AlertaCritica", "R2_ProtocoloDefensiva"])

    def test_conservacion_hechos_iniciales(self):
        """Verificar que la función de inferencia no muta ni altera el conjunto de hechos originales."""
        hechos_iniciales = {"alta_latencia_red", "fallo_autenticacion_api"}
        copia_original = set(hechos_iniciales)
        
        inferir(hechos_iniciales, REGLAS_PROYECTO)
        self.assertEqual(hechos_iniciales, copia_original)

    def test_prevencion_ciclos_infinitos(self):
        """Verificar que reglas circulares o reflexivas no provocan un bucle infinito en el motor."""
        reglas_ciclicas = [
            Regla("RC1", frozenset({"a"}), "b"),
            Regla("RC2", frozenset({"b"}), "a")  # Ciclo a -> b -> a
        ]
        hechos_iniciales = {"a"}
        
        # Si el motor tuviera un fallo de control de duplicados, colgaría la ejecución.
        hechos_finales, traza = inferir(hechos_iniciales, reglas_ciclicas)
        self.assertIn("b", hechos_finales)
        self.assertEqual(traza, ["RC1"]) # RC2 no se vuelve a disparar porque 'a' ya estaba en los hechos

if __name__ == "__main__":
    unittest.main()