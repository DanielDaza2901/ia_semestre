from pathlib import Path
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

DATA_DIR = Path("data")
REPORTS_DIR = Path("reports")
KB_PATH = DATA_DIR / "base_conocimiento.txt"
REPORT_PATH = REPORTS_DIR / "semana05.md"

DEFAULT_DOCS = [
    "Un equipo caliente o con temperatura alta requiere revisar la ventilación y el disipador.",
    "Una falla de red o error de DNS en internet requiere revisar la conectividad y el enlace principal.",
    "Una aplicación lenta requiere revisar el uso de CPU, memoria RAM y disco.",
    "Una cuenta bloqueada o problemas de inicio de sesión requieren revisar permisos de usuario.",
    "Un error de impresora o atasco de papel requiere verificar bandejas y reiniciar servicios.",
    "Una pantalla azul de Windows (BSOD) indica conflictos de controladores o fallas de hardware.",
    "Un certificado SSL expirado genera errores de seguridad en el navegador y requiere renovación.",
    "Un espacio en disco insuficiente afecta el rendimiento y requiere limpieza de temporales."
]

# MEJORA: Reglas expertas basadas en Expresiones Regulares (Regex) para detección precisa de patrones
RULES = [
    (lambda q: bool(re.search(r"\b(temperatura|caliente|calentamiento)\b", q)), "revisar_ventilacion"),
    (lambda q: bool(re.search(r"\b(red|internet|dns|conexion)\b", q)), "revisar_conectividad"),
    (lambda q: bool(re.search(r"\b(lenta|memoria|cpu|disco)\b", q)), "revisar_rendimiento"),
    (lambda q: bool(re.search(r"\b(sesion|cuenta|bloqueada|contrasena|acceso)\b", q)), "revisar_acceso"),
    (lambda q: bool(re.search(r"\b(impresora|papel|imprimir)\b", q)), "revisar_hardware_impresion"),
]

TRAIN_X = [
    "equipo muy caliente y ventilador", "temperatura alta en el procesador",
    "se cae internet", "error de dns constante", "falla de red local",
    "aplicacion lenta", "consumo alto de cpu y memoria", "disco lleno",
    "no puedo iniciar sesion", "cuenta bloqueada", "error de contraseña",
    "atasco de papel en impresora", "la impresora no imprime",
    "pantalla azul de windows", "error critico de driver"
]

TRAIN_Y = [
    "hardware", "hardware", "red", "red", "red",
    "rendimiento", "rendimiento", "rendimiento",
    "seguridad", "seguridad", "seguridad",
    "hardware", "hardware", "hardware", "hardware"
]

def load_documents() -> list[str]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not KB_PATH.exists():
        KB_PATH.write_text("\n".join(DEFAULT_DOCS), encoding="utf-8")
    docs = [line.strip() for line in KB_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(docs) < 8:
        raise ValueError("data/base_conocimiento.txt debe contener al menos 8 entradas.")
    return docs

DOCS = load_documents()
vectorizer = TfidfVectorizer()
doc_matrix = vectorizer.fit_transform(DOCS)

classifier = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000, random_state=42),
)
classifier.fit(TRAIN_X, TRAIN_Y)

def answer(query: str, threshold: float = 0.25) -> dict:
    q = query.lower()
    fired = [name for condition, name in RULES if condition(q)]
    
    similarities = cosine_similarity(vectorizer.transform([q]), doc_matrix)[0]
    best_index = int(similarities.argmax())
    best_sim = float(similarities[best_index])
    
    # MEJORA: Umbral de confianza y rechazo para filtrar evidencias de baja relevancia
    if best_sim < threshold:
        evidencia = "No se encontró evidencia suficiente en la base de conocimiento (por debajo del umbral)."
    else:
        evidencia = DOCS[best_index]
        
    label = str(classifier.predict([q])[0])
    
    return {
        "reglas": fired,
        "evidencia": evidencia,
        "similitud": best_sim,
        "clase": label,
    }

def write_report(rows: list[tuple[str, dict]]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    lines = ["# Semana 05 - Sistema Híbrido Optimizado (Soporte Técnico)", ""]
    for i, (query, result) in enumerate(rows, start=1):
        lines += [
            f"## Consulta {i}",
            f"- **Entrada:** {query}",
            f"- **Reglas Disparadas (Regex):** {', '.join(result['reglas']) or 'ninguna'}",
            f"- **Evidencia Recuperada:** {result['evidencia']}",
            f"- **Similitud Coseno:** {result['similitud']:.3f}",
            f"- **Clase Predicha:** {result['clase']}",
            ""
        ]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    queries = [
        "El equipo esta muy caliente y el ventilador hace ruido",
        "No puedo iniciar sesion con mi cuenta institucional",
        "Se cae el internet y aparece un error de dns",
        "Consulta completamente ambigua sin relacion tecnica alguna 12345" # Prueba de umbral de rechazo
    ]
    
    results = []
    print("=== Ejecución del Sistema Híbrido Optimizado (Semana 05) ===")
    for q in queries:
        res = answer(q, threshold=0.25)
        results.append((q, res))
        print(f"\nConsulta: {q}")
        print(res)
        
    write_report(results)
    
    # MEJORA: Imprimir reporte de métricas del clasificador en consola
    print("\n=== Evaluación del Clasificador (Classification Report) ===")
    preds = classifier.predict(TRAIN_X)
    print(classification_report(TRAIN_Y, preds))
    
    print(f"Reporte avanzado generado exitosamente en: {REPORT_PATH}")