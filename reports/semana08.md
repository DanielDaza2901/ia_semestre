# Informe Técnico - Semana 08: Sistema Inteligente de Reconocimiento Integrado

## 1. Introducción
Este informe documenta la integración de un flujo completo de inteligencia artificial que combina una Red Neuronal Artificial (MLP) para reconocimiento de patrones, persistencia de evidencias en base de datos relacional (SQLite) y representación formal del conocimiento mediante una ontología en grafos (GraphML).

---

## 2. Arquitectura del Sistema
El flujo conecta tres componentes principales:
1. **Modelo de Reconocimiento (MLP):** Procesa características numéricas de entradas normalizadas (vectores de imágenes de dígitos).
2. **Registro de Evidencia (SQLite):** Almacena metadatos y trazabilidad en `artifacts/imagenes.db`.
3. **Interpretación Semántica (Ontología GraphML):** Modela conceptos y relaciones lógicas que traducen la predicción en un significado dentro del dominio.

---

## 3. Análisis de Componentes
* **Red Neuronal:** Reconoce patrones estructurales asociados a clases discretas con alta exactitud (*Accuracy* superior al 95%).
* **Base de Datos:** Garantiza la trazabilidad auditable de las muestras y metadatos analizados.
* **Ontología:** Establece relaciones expresivas con verbo y sentido directo (ej. `modelo_mlp reconoce digito`, `prediccion asigna_clase digito`), vinculando dinámicamente casos de prueba con su concepto ontológico.

---

## 4. Limitaciones Encontradas
* La red neuronal MLP es sensible a variaciones espaciales extremas (como rotaciones de la imagen), requiriendo arquitecturas convolucionales en entornos de producción más complejos.

---

## 5. Conclusiones
* La combinación de reconocimiento neuronal, bases de datos y ontologías resuelve el problema de la explicabilidad en IA, permitiendo predecir, auditar y contextualizar los resultados.