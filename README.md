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

* `src/`: Contiene los códigos fuente en Python (ej. modelos de clasificación).
* `data/`: Directorio destinado a los conjuntos de datos de las prácticas.
* `notebooks/`: Cuadernos interactivos de Jupyter para experimentación y análisis exploratorio.
* `artifacts/`: Archivos generados, modelos entrenados o serializados.
* `reports/`: Informes técnicos y documentación de los resultados.
* `tests/`: Pruebas unitarias y de integración del código.

## 🛠️ Requisitos e Instalación

1. Clona el repositorio e ingresa a la carpeta del proyecto.
2. Activa el entorno virtual:
   ```bash
   .venv\Scripts\Activate.ps1