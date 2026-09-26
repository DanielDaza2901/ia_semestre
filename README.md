# IA Semestre - Práctica de Fundamentos y Modelos Predictivos

Repositorio oficial para las prácticas del semestre de Inteligencia Artificial. Contiene la estructura base, entornos virtuales configurados y scripts reproducibles de Machine Learning.

## Módulos Desarrollados y Avances Semanales

### Semana 02: Fundamentos
- Configuración del entorno de desarrollo y estructura inicial del proyecto.
- Definición de la arquitectura base y organización de directorios.

### Semana 03: Taxonomía de Inteligencia Artificial
- **Propósito:** Construcción de un motor clasificador simbólico de requerimientos para categorizar problemas de IA.
- **Implementación:** Script (`src/semana03_taxonomia.py`) capaz de asignar categorías de IA basándose en palabras clave con pesos semánticos ponderados.
- **Resultados y Hallazgos:** 
    - Clasificación automática con **100% de coincidencia** (20/20 casos) respecto a la referencia manual.
    - Implementación de un sistema de pesos enteros (1 a 3) en las reglas personalizadas (`CUSTOM_RULES`) para mitigar ambigüedades en problemas complejos.
    - Generación automática del informe técnico de auditoría en `reports/semana03.md`.

### Semana 04: Marco Tecnológico de la Inteligencia Artificial
- **Propósito:** Implementación de algoritmos de búsqueda informada ($A^*$) y toma de decisiones en entornos adversariales (Minimax optimizado con Poda Alfa-Beta).
- **Implementación:** 
  - `src/semana04_astar.py`: Planificación de rutas óptimas mediante heurística de distancia Manhattan y renderizado gráfico de la cuadrícula.
  - `src/semana04_minimax.py`: Selección de jugadas racionales en un entorno de juego adversarial aplicando acotamiento mediante poda alfa-beta.
- **Evidencia y Resultados:** Documentación detallada de estados, acciones, costos y análisis de ingeniería en `reports/semana04.md`.
---
### Semana 05: Marco Tecnológico de la Inteligencia Artificial (Sistema Híbrido)
- **Propósito:** Construcción de un sistema híbrido trazable que combina reglas expertas deterministas (Regex), recuperación de información documental (TF-IDF y similitud coseno) y clasificación supervisada de texto (Regresión Logística).
- **Implementación:** 
  - `src/semana05_sistema_hibrido.py`: Script optimizado que integra reglas expertas basadas en expresiones regulares, un umbral de confianza y rechazo dinámico para entradas ambiguas, y evaluación cuantitativa de métricas de rendimiento.
- **Evidencia y Resultados:** Reporte técnico detallado con trazabilidad de reglas disparadas, evidencias recuperadas, similitudes, clasificación y métricas globales (*accuracy* del 93%) en `reports/semana05.md`.
### Semana 07: Representaciones del Reconocimiento
- **Propósito:** Aplicar e integrar tres formas fundamentales de representación del conocimiento sobre un mismo fenómeno técnico: métodos numéricos, métodos simbólicos y reconocimiento mediante autómatas finitos.
- **Implementación:** 
  - `src/semana07_representaciones.py`: Script modular que ejecuta la representación numérica (cálculo de distancias euclidianas y vectores de características de servidores), la representación simbólica (evaluación de conjuntos de hechos mediante reglas lógicas `SI-ENTONCES`) y un autómata finito determinista para el reconocimiento de secuencias de eventos de red.
- **Evidencia y Resultados:** Generación del informe técnico comparativo en `reports/semana07.md` detallando las ventajas, limitaciones y la pérdida de información inherente a cada enfoque representacional.
### Semana 08: Sistema Inteligente de Reconocimiento Integrado
- **Propósito:** Integrar un flujo completo de inteligencia artificial que combina una red neuronal artificial (MLP) para reconocimiento de patrones, persistencia de evidencias en base de datos relacional (SQLite) y representación formal del conocimiento mediante una ontología en grafos (GraphML).
- **Implementación:** 
  - `src/semana08_red_ontologia.py`: Script que entrena el clasificador neuronal, valida su exactitud, almacena metadatos de auditoría en SQLite y vincula dinámicamente las predicciones con conceptos ontológicos.
- **Evidencia y Resultados:** Generación exitosa de artefactos serializados (`modelo_mlp.pkl`, `imagenes.db`, `ontologia.graphml`) en la carpeta `artifacts/` y del informe técnico completo en `reports/semana08.md`.
---
---
---

## Arquitectura del Proyecto

Proyecto estructurado para garantizar la modularidad, reproducibilidad y escalabilidad de modelos de IA.

## 🛠 Stack Tecnológico

### Lenguaje y Entorno
- **Python 3.13** - Lenguaje principal.
- **venv** - Gestión de entornos virtuales aislados.

### Ciencia de Datos
- **NumPy** - Procesamiento numérico.
- **Pandas** - Manipulación de datos.
- **Scikit-learn** - Modelos de Machine Learning.
- **Matplotlib** - Visualización de datos.

### Desarrollo y Control de Versiones
- **Git** - Control de versiones.
- **VS Code** - Entorno de desarrollo.

## Instalación

### Pre-requisitos
- Node.js >= 18.x (opcional para herramientas web).
- Python 3.13+.
- Git.

### Clonar el repositorio
```bash
git clone [https://github.com/DanielDaza2901/ia_semestre.git](https://github.com/DanielDaza2901/ia_semestre.git)
cd ia_semestre
Configurar Entorno
Bash
# Crear entorno virtual
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Instalar dependencias
python -m pip install -r requirements.txt

---

## Estructura del Proyecto
Plaintext
## Estructura del Repositorio
ia_semestre/
├── .venv/            # Entorno virtual
├── artifacts/        # Modelos serializados (.pkl, .joblib)
├── data/             # Datasets (CSV, JSON, etc.)
├── notebooks/        # Experimentación interactiva (Jupyter)
├── reports/          # Informes técnicos (.md, .pdf)
├── src/              # Código fuente (scripts de entrenamiento)
│   └── semana02/     # Actividades semanales
├── tests/            # Pruebas unitarias
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación principal

---

Autor
- Estudiante: Daniel Eduardo Daza Cuello
- Institución: ETITC - 10º Semestre

