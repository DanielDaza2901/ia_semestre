"""
Módulo de Motor de Inferencia y Sistemas Lógicos - Semana 13
Autor: Daniel Eduardo Daza Cuello (ETITC - Ingeniería de Sistemas)
Propósito: Implementar un motor de inferencia basado en reglas con encadenamiento hacia adelante,
trazabilidad y prevención de duplicados/ciclos para el proyecto individual.
"""

from dataclasses import dataclass
from typing import Set, List, Tuple, FrozenSet

@dataclass(frozen=True)
class Regla:
    """Estructura inmutable para representar una regla lógica (Premisas -> Conclusión)."""
    nombre: str
    premisas: FrozenSet[str]
    conclusion: str

def inferir(hechos_iniciales: Set[str], reglas: List[Regla]) -> Tuple[Set[str], List[str]]:
    """
    Ejecuta el motor de inferencia por encadenamiento hacia adelante.
    
    Parámetros:
    - hechos_iniciales: Conjunto inicial de proposiciones verdaderas.
    - reglas: Lista de objetos Regla disponibles en la base de conocimientos.
    
    Retorna:
    - hechos: Conjunto ampliado con hechos iniciales e inferidos.
    - trazas: Historial ordenado de los nombres de las reglas ejecutadas.
    """
    # Copia de seguridad para no mutar los hechos iniciales de entrada
    hechos = set(hechos_iniciales)
    trazas: List[str] = []
    cambios = True

    while cambios:
        cambios = False
        for regla in reglas:
            # Comprobar si todas las premisas están presentes y la conclusión es completamente nueva
            if regla.premisas.issubset(hechos) and regla.conclusion not in hechos:
                hechos.add(regla.conclusion)
                trazas.append(regla.nombre)
                cambios = True  # Hubo un nuevo hecho, otra ronda es necesaria

    return hechos, trazas

# ==========================================
# DEFINICIÓN DE LA BASE DE CONOCIMIENTO (PROYECTO TI)
# ==========================================
# 3 Reglas originales del dominio de automatización de soporte técnico:
REGLAS_PROYECTO = [
    Regla(
        nombre="R1_AlertaCritica",
        premisas=frozenset({"alta_latencia_red", "fallo_autenticacion_api"}),
        conclusion="amenaza_seguridad_detectada"
    ),
    Regla(
        nombre="R2_ProtocoloDefensiva",
        premisas=frozenset({"amenaza_seguridad_detectada", "firewall_activo"}),
        conclusion="aislamiento_segmento_requerido"
    ),
    Regla(
        nombre="R3_NotificacionAutomatica",
        premisas=frozenset({"aislamiento_segmento_requerido", "canal_notificacion_operativo"}),
        conclusion="alerta_incidente_despachada"
    )
]

if __name__ == "__main__":
    print("=== DEMOSTRACIÓN DEL MOTOR DE INFERENCIA (CASO A: Demostrado) ===" )
    hechos_caso_a = {
        "alta_latencia_red", 
        "fallo_autenticacion_api", 
        "firewall_activo", 
        "canal_notificacion_operativo"
    }
    
    resultado_a, traza_a = inferir(hechos_caso_a, REGLAS_PROYECTO)
    print(f"Hechos iniciales: {hechos_caso_a}")
    print(f"Hechos finales inferidos: {resultado_a}")
    print(f"Trazabilidad de ejecución: {traza_a}")
    print(f"¿Conclusión 'alerta_incidente_despachada' demostrada?: {'alerta_incidente_despachada' in resultado_a}")

    print("\n=== DEMOSTRACIÓN DEL MOTOR DE INFERENCIA (CASO B: No demostrado) ===" )
    # Caso B: Sin canal de notificación operativo, por lo que R3 no debe dispararse
    hechos_caso_b = {
        "alta_latencia_red", 
        "fallo_autenticacion_api", 
        "firewall_activo"
        # Falta "canal_notificacion_operativo"
    }
    
    resultado_b, traza_b = inferir(hechos_caso_b, REGLAS_PROYECTO)
    print(f"Hechos iniciales: {hechos_caso_b}")
    print(f"Hechos finales inferidos: {resultado_b}")
    print(f"Trazabilidad de ejecución: {traza_b}")
    print(f"¿Conclusión 'alerta_incidente_despachada' demostrada?: {'alerta_incidente_despachada' in resultado_b}")
    print("Nota: Una conclusión no demostrada NO significa que sea falsa, simplemente faltó evidencia positiva.")