import numpy as np

print("=== 1. REPRESENTACIÓN NUMÉRICA (Métricas de Servidor) ===")
# Vector que representa el estado actual de un servidor: [uso_cpu (%), uso_memoria (%), latencia (ms)]
sample = np.array([85.5, 90.0, 120.0])
reference = np.array([50.0, 60.0, 40.0]) # Valores óptimos de referencia

# Cálculo de distancia euclidiana para medir la desviación del estado óptimo
distance = np.linalg.norm(sample - reference)
print(f"Vector actual: {sample}")
print(f"Vector de referencia óptima: {reference}")
print(f"Distancia numérica a la normalidad: {round(float(distance), 3)}\n")


print("=== 2. REPRESENTACIÓN SIMBÓLICA (Hechos y Reglas Expertas) ===")
# Definición de hechos conocidos extraídos del análisis del sistema
facts = {"cpu_alto", "memoria_saturada", "latencia_elevada"}
print(f"Hechos activos en el sistema: {facts}")

# Regla simbólica: SI se cumplen condiciones críticas -> ENTONCES conclusión diagnóstica
if {"cpu_alto", "memoria_saturada"}.issubset(facts):
    print("Conclusión simbólica generada: ALERTA_CRITICA_INFRAESTRUCTURA\n")


print("=== 3. AUTÓMATA FINITO (Reconocimiento de Patrones de Eventos) ===")
# Autómata que reconoce secuencias de eventos de red que terminan en '10' 
# (Alfabeto: {'0', '1'}, donde 1 = evento de advertencia, 0 = evento normal)
def accepts_ends_with_10(text):
    state = "q0"
    # Tabla de transiciones formal del autómata
    transitions = {
        ("q0", "0"): "q0", ("q0", "1"): "q1",
        ("q1", "0"): "q2", ("q1", "1"): "q1",
        ("q2", "0"): "q0", ("q2", "1"): "q1",
    }
    for symbol in text:
        if (state, symbol) in transitions:
            state = transitions[(state, symbol)]
        else:
            return False
    return state == "q2"  # q2 es el estado de aceptación

# Pruebas de secuencias de eventos
secuencias_prueba = ["1110", "0010", "1011", "0101"]
print("Alfabeto: {'0', '1'} | Patrón de aceptación: Secuencias que terminan en '10'")
for seq in secuencias_prueba:
    print(f"Secuencia de eventos '{seq}' -> Aceptada: {accepts_ends_with_10(seq)}")