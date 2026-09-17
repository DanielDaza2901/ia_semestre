# Informe Técnico - Semana 07: Representaciones del Reconocimiento

## 1. Introducción
En los sistemas inteligentes, un mismo fenómeno del mundo real (como el comportamiento de un servidor o una incidencia técnica) puede ser representado de múltiples formas. La elección de la representación determina qué operaciones matemáticas o lógicas puede realizar el algoritmo y qué información se prioriza o descartara.

---

## 2. Implementación en el Proyecto
El script desarrollado en `src/semana07_representaciones.py` modela el estado operativo de un nodo tecnológico utilizando:
1. **Representación Numérica:** Vectores en espacios continuos para calcular desvíos mediante normas vectoriales.
2. **Representación Simbólica:** Conjuntos discretos de hechos evaluados mediante implicaciones lógicas (reglas SI-ENTONCES).
3. **Autómata Finito:** Máquina de estados para reconocer patrones secuenciales discretos en los logs de eventos.

---

## 3. Tabla Comparativa de Representaciones

| Representación | Qué información utiliza | Qué puede reconocer | Ventajas | Limitaciones | Información que puede perderse |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Numérica** | Valores cuantitativos continuos (ej. porcentajes de CPU, memoria y latencia). | Grados de similitud, distancias métricas y desvíos cuantitativos respecto a un óptimo. | Permite cálculos estadísticos precisos, operaciones continuas y análisis vectorial rápido. | Falta de explicabilidad semántica directa; sensibilidad a escalas y unidades métricas. | El contexto cualitativo y las relaciones lógicas entre las variables (el "por qué"). |
| **Simbólica** | Conceptos discretos, etiquetas categóricas y relaciones lógicas explícitas. | Hechos complejos, causa-efecto y diagnósticos altamente explicables. | Alta interpretabilidad humana, facilidad para auditorías y aplicación directa de reglas expertas. | Rigidez ante datos imprecisos o continuos; dificultad para manejar incertidumbre numérica directa. | Matices graduales, variaciones continuas y la magnitud exacta de las desviaciones. |
| **Autómata** | Secuencias ordenadas de símbolos discretos pertenecientes a un alfabeto definido. | Patrones temporales exactos, gramáticas regulares y secuencias de estados válidas. | Eficiencia computacional extrema ($O(n)$), formalismo matemático riguroso y claridad absoluta en transiciones. | Incapacidad para procesar valores numéricos continuos o relaciones complejas fuera del orden secuencial. | Magnitudes temporales reales, pesos cuantitativos y contextos globales fuera de la secuencia lineal. |

---

## 4. Conclusiones
* Ninguna representación es superior por sí sola; en la ingeniería de sistemas inteligentes, los sistemas híbridos se benefician al traducir datos numéricos crudos a símbolos estructurados, y validando secuencias operativas mediante autómatas formales.
* La pérdida de información es inherente al proceso de abstracción, por lo que el diseño arquitectónico debe alinear la representación con los requerimientos específicos de decisión y trazabilidad del proyecto.