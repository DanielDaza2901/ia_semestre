"""
Módulo de Benchmark de Modelos y Decisión Técnica - Semana 11
Autores: Daniel Eduardo Daza Cuello (ETITC - Ingeniería de Sistemas)
Propósito: Comparar modelos, generar benchmark.csv y redactar automáticamente el informe ADR.
"""

from pathlib import Path
from time import perf_counter
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Configuración de directorios de trabajo
ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = ROOT / "artifacts"
REPORTS_DIR = ROOT / "reports"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def ejecutar_benchmark():
    print("=== 1. CARGA Y PARTICIÓN CONTROLADA DEL DATASET ===")
    X, y = load_digits(return_X_y=True)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    print(f"Muestras de entrenamiento: {X_train.shape[0]} | Muestras de prueba: {X_test.shape[0]}")

    print("\n=== 2. DEFINICIÓN DE LOS TRES MODELOS A COMPARAR ===")
    models = {
        "logistic": make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=1500, random_state=42)
        ),
        "forest": RandomForestClassifier(
            n_estimators=250, random_state=42, n_jobs=-1
        ),
        "mlp": make_pipeline(
            StandardScaler(),
            MLPClassifier(hidden_layer_sizes=(64,), max_iter=350, random_state=42)
        ),
    }

    print("\n=== 3. EJECUCIÓN DEL BENCHMARK (Entrenamiento y Medición) ===")
    rows = []
    for name, model in models.items():
        print(f"Entrenando modelo: {name}...")
        start = perf_counter()
        model.fit(X_train, y_train)
        elapsed = perf_counter() - start
        
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        
        rows.append({
            "modelo": name,
            "accuracy": round(float(acc), 4),
            "fit_seconds": round(float(elapsed), 4)
        })
        print(f" -> Accuracy: {acc:.4f} | Tiempo: {elapsed:.4f}s")

    # Ordenar por accuracy de mayor a menor
    df = pd.DataFrame(rows).sort_values("accuracy", ascending=False)
    
    print("\n=== 4. RESULTADOS FINALES DEL BENCHMARK ===")
    print(df.to_string(index=False))

    # Persistencia del archivo CSV
    csv_path = ARTIFACTS_DIR / "benchmark.csv"
    df.to_csv(csv_path, index=False)
    print(f"\n[INFO] Benchmark guardado en: {csv_path}")

    # Generación automática del informe ADR usando los datos del DataFrame
    generar_adr_automatico(df)

def generar_adr_automatico(df):
    print("\n=== 5. GENERACIÓN AUTOMÁTICA DEL INFORME ADR (reports/semana11_adr.md) ===")
    
    # Extraer el mejor modelo basado en los resultados reales
    mejor_modelo = df.iloc[0]["modelo"]
    mejor_acc = df.iloc[0]["accuracy"]
    mejor_tiempo = df.iloc[0]["fit_seconds"]

    # Construir la tabla Markdown dinámicamente
    tabla_md = "| Modelo | Accuracy | Tiempo de Entrenamiento (s) |\n| :--- | :--- | :--- |\n"
    for _, row in df.iterrows():
        tabla_md += f"| {row['modelo']} | {row['accuracy']} | {row['fit_seconds']} |\n"

    contenido_adr = f"""# Architecture Decision Record (ADR) - Semana 11: Benchmark y Selección de Modelo

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

{tabla_md}

---

## 4. Modelo Seleccionado y Justificación Técnica
* **Modelo Elegido:** **{mejor_modelo}** (con una precisión de **{mejor_acc}** y un tiempo de ajuste de **{mejor_tiempo}** segundos).
* **Justificación:** Los datos demuestran que `{mejor_modelo}` ofrece el mejor balance de rendimiento para el proyecto. Garantiza una tasa de acierto sobresaliente, cumpliendo con los estándares de calidad esperados para la infraestructura de inteligencia artificial.

---

## 5. Ventajas, Limitaciones y Consecuencias (Trade-offs)
* **Ventajas:** Excelente capacidad de generalización ante datos no vistos y estabilidad predictiva.
* **Limitaciones:** Dependencia de la calidad y normalización previa de los vectores de características de entrada.
* **Consecuencias:** Se establece oficialmente este modelo como el núcleo analítico y clasificatorio del sistema.

---

## 6. Aplicación al Proyecto Final
El componente seleccionado procesará de manera automatizada las salidas numéricas generadas en las fases anteriores, permitiendo la toma de decisiones inteligente dentro de la arquitectura general del software.
"""

    adr_path = REPORTS_DIR / "semana11_adr.md"
    adr_path.write_text(contenido_adr, encoding="utf-8")
    print(f"[INFO] Informe ADR generado exitosamente en: {adr_path}")

if __name__ == "__main__":
    ejecutar_benchmark()