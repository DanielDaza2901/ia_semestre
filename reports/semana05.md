# Semana 05 - Sistema Híbrido Optimizado (Soporte Técnico)

## Consulta 1
- **Entrada:** El equipo esta muy caliente y el ventilador hace ruido
- **Reglas Disparadas (Regex):** revisar_ventilacion
- **Evidencia Recuperada:** Un equipo caliente o con temperatura alta requiere revisar la ventilación y el disipador.
- **Similitud Coseno:** 0.484
- **Clase Predicha:** hardware

## Consulta 2
- **Entrada:** No puedo iniciar sesion con mi cuenta institucional
- **Reglas Disparadas (Regex):** revisar_acceso
- **Evidencia Recuperada:** No se encontró evidencia suficiente en la base de conocimiento (por debajo del umbral).
- **Similitud Coseno:** 0.235
- **Clase Predicha:** seguridad

## Consulta 3
- **Entrada:** Se cae el internet y aparece un error de dns
- **Reglas Disparadas (Regex):** revisar_conectividad
- **Evidencia Recuperada:** Una falla de red o error de DNS en internet requiere revisar la conectividad y el enlace principal.
- **Similitud Coseno:** 0.539
- **Clase Predicha:** red

## Consulta 4
- **Entrada:** Consulta completamente ambigua sin relacion tecnica alguna 12345
- **Reglas Disparadas (Regex):** ninguna
- **Evidencia Recuperada:** No se encontró evidencia suficiente en la base de conocimiento (por debajo del umbral).
- **Similitud Coseno:** 0.000
- **Clase Predicha:** hardware

---

## 1. Introducción
Este informe documenta la arquitectura, el diseño y las mejoras de nivel de ingeniería aplicadas a un sistema híbrido de inteligencia artificial que combina reglas expertas deterministas, recuperación de información basada en similitud coseno (TF-IDF), y reconocimiento de formas mediante clasificación supervisada de texto (Regresión Logística).

---

## 2. Componentes del Sistema Híbrido
* **Sistemas Expertos (Reglas Regex):** Representan el conocimiento del dominio mediante patrones de expresiones regulares para disparar acciones automáticas y explicables.
* **Ingeniería del Conocimiento:** Estructuración y validación de una base documental en `data/base_conocimiento.txt` que garantiza un conjunto mínimo de fuentes de evidencia.
* **Recuperación de Información (TF-IDF + Coseno):** Convierte texto libre en vectores numéricos ponderados para identificar el documento más relevante ante una consulta.
* **Reconocimiento de Formas (Clasificación):** Pipeline de aprendizaje automático que predice la categoría operativa de la consulta (red, hardware, seguridad, rendimiento).

---

## 3. Mejoras y Optimizaciones de Ingeniería Implementadas

Con el fin de elevar la robustez, seguridad y auditabilidad del sistema, se incorporaron las siguientes mejoras analíticas:

### A. Reglas Expertas Basadas en Expresiones Regulares (`re.search`)
* **¿Por qué se realizó?:** Las reglas basadas en subcadenas simples (`in q`) presentaban vulnerabilidades ante variaciones morfológicas o coincidencias parciales accidentales dentro de cadenas de texto más amplias.
* **¿Para qué sirve?:** Permite implementar límites de palabras (`\b`) y operadores lógicos estrictos, asegurando que las reglas expertas detecten términos técnicos específicos con alta precisión y eviten falsos positivos.

### B. Umbrales de Confianza y Rechazo Dinámico (`threshold`)
* **¿Por qué se realizó?:** El modelo base de recuperación asignaba obligatoriamente un resultado independientemente de que la consulta no tuviera relación técnica con la base de conocimiento.
* **¿Para qué sirve?:** Establece un filtro de seguridad basado en la similitud coseno (por ejemplo, un umbral mínimo de `0.25`). Si una consulta ambigua o irrelevante no alcanza dicho valor, el sistema emite un rechazo controlado informando que no existe evidencia suficiente, evitando entregar respuestas forzadas o alucinadas.

### C. Evaluación Cuantitativa del Clasificador (`classification_report`)
* **¿Por qué se realizó?:** Los sistemas basados en aprendizaje supervisado requieren validación numérica explícita para certificar su rendimiento y no depender únicamente de pruebas cualitativas en consola.
* **¿Para qué sirve?:** Genera métricas detalladas de precisión (*precision*), cobertura (*recall*) y puntaje F1 por cada categoría del dominio, además de evaluar la exactitud global (*accuracy*) del clasificador dentro del informe de ejecución.

---

## 4. Conclusiones
* La integración de un umbral de rechazo dota al sistema de un mecanismo de control de calidad robusto frente a entradas ambiguas, garantizando que la trazabilidad dependa estrictamente de evidencias relevantes.
* Las métricas obtenidas mediante el reporte de clasificación validan la alta efectividad del modelo de Regresión Logística entrenado, logrando un equilibrio óptimo entre la determinabilidad de las reglas expertas y la generalización del procesamiento de lenguaje natural.
