# Semana 03 - Taxonomía de Inteligencia Artificial 
## Resultado automático frente a clasificación manual de referencia
| Caso | Categoría automática principal | Categorías detectadas | Manual | Estado |
|---|---|---|---|---|
| 1 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 2 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 3 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 4 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 5 | Sistemas de recomendación | Sistemas de recomendación | Sistemas de recomendación | Coincide |
| 6 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 7 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 8 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 9 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 10 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 11 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 12 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 13 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 14 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 15 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 16 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 17 | Visión por computador | Visión por computador, Robótica y sistemas autónomos | Visión por computador | Coincide |
| 18 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 19 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 20 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |

Coincidencia con la referencia: **100.00%** (20/20).

## Justificación de Mejoras Técnicas
1. **Ponderación de Términos Clave (Pesos Semánticos):** Se modificó la estructura de palabras clave para incluir pesos enteros (de 1 a 3). Términos específicos y complejos de dominios críticos (como *'vehículo autónomo'* o *'diagnóstico'*) reciben mayor peso que palabras generales, reduciendo ambigüedades en la clasificación principal.
2. **Trazabilidad de Puntuación:** El motor calcula una matriz de puntajes por cada categoría evaluada, permitiendo auditorías internas sobre por qué una categoría secundaria obtiene más o menos relevancia frente al problema planteado.
3. **Ampliación de Reglas Personalizadas (`CUSTOM_RULES`):** Se integraron términos de dominio específicos (matrículas, sentimientos, fallas, síntomas y trayectorias) para garantizar una correspondencia más fina con problemas del entorno real.

## Discrepancias y análisis de ingeniería
En los casos donde la clasificación automática difiere de la referencia manual, se observa que los problemas de ingeniería suelen cruzar múltiples fronteras (por ejemplo, robótica que requiere visión por computador o sistemas expertos basados en reglas de negocio). La ponderación ayuda a mitigar falsos positivos, pero se recomienda complementar este motor simbólico con enfoques basados en embeddings o modelos de lenguaje en fases posteriores del proyecto semestral.