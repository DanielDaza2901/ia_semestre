# Architecture Decision Record (ADR) - Semana 11: Benchmark y Selección de Modelo

## 1. Contexto del Problema
El sistema requiere clasificar de forma automatizada los patrones y características numéricas extraídas del dominio del proyecto. Para garantizar un rendimiento óptimo en producción, es necesario seleccionar rigurosamente un modelo de clasificación basado en evidencia cuantitativa.

---

## 2. Modelos Evaluados (Alternativas)
Se evaluaron tres arquitecturas bajo exactamente el mismo protocolo experimental (`train_test_split` con semilla 42, estratificación y normalización con `StandardScaler`):
1. **Logistic Regression:** Modelo lineal simple, altamente interpretable y de bajísimo costo computacional (línea base).
2. **Random Forest:** Ensamble de árboles de decisión robusto frente a relaciones no lineales y capaz de manejar interacciones complejas.
3. **MLPClassifier (Red Neuronal Multicapa):** Modelo basado en aprendizaje profundo superficial, ideal para capturar patrones abstractos complejos.

---

## 3. Resultados Obtenidos (Benchmark Automatizado)
A partir de la ejecución registrada en `artifacts/benchmark.csv`, se obtuvieron las siguientes métricas de rendimiento:

| Modelo | Accuracy | Tiempo de Entrenamiento (s) |
| :--- | :--- | :--- |
| mlp | 0.98 | 3.1928 |
| logistic | 0.9778 | 0.0547 |
| forest | 0.9667 | 0.6052 |


---

## 4. Modelo Seleccionado y Justificación Técnica
* **Modelo Elegido:** **mlp** (con una precisión de **0.98** y un tiempo de ajuste de **3.1928** segundos).
* **Justificación:** Los datos demuestran que `mlp` ofrece el mejor balance de rendimiento para el proyecto. Garantiza una tasa de acierto sobresaliente, cumpliendo con los estándares de calidad esperados para la infraestructura de inteligencia artificial.

---

## 5. Ventajas, Limitaciones y Consecuencias (Trade-offs)
* **Ventajas:** Excelente capacidad de generalización ante datos no vistos y estabilidad predictiva.
* **Limitaciones:** Dependencia de la calidad y normalización previa de los vectores de características de entrada.
* **Consecuencias:** Se establece oficialmente este modelo como el núcleo analítico y clasificatorio del sistema.

---

## 6. Aplicación al Proyecto Final
El componente seleccionado procesará de manera automatizada las salidas numéricas generadas en las fases anteriores, permitiendo la toma de decisiones inteligente dentro de la arquitectura general del software.
