from pathlib import Path
import pickle
import sqlite3
import networkx as nx
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Configuración de rutas
ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(parents=True, exist_ok=True)

print("=== 1. CARGA DE DATOS Y PARTICIÓN (TRAIN / TEST) ===")
X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print(f"Total muestras: {X.shape[0]} | Entrenamiento: {X_train.shape[0]} | Prueba: {X_test.shape[0]}")


print("\n=== 2. ENTRENAMIENTO DEL MODELO DE RECONOCIMIENTO (MLP) ===")
model = MLPClassifier(
    hidden_layer_sizes=(64,),
    max_iter=400,
    random_state=42
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print(f"Accuracy de la Red Neuronal (MLP): {round(acc, 4) * 100}%")

model_path = ARTIFACTS / "modelo_mlp.pkl"
with model_path.open("wb") as file:
    pickle.dump(model, file)
print(f"Modelo guardado en: {model_path}")


print("\n=== 3. REGISTRO DE EVIDENCIA EN BASE DE DATOS (SQLite) ===")
db_path = ARTIFACTS / "imagenes.db"
with sqlite3.connect(db_path) as con:
    con.execute(
        "CREATE TABLE IF NOT EXISTS images("
        "id INTEGER PRIMARY KEY, label INTEGER, split TEXT)"
    )
    con.execute("DELETE FROM images")
    con.executemany(
        "INSERT INTO images(id, label, split) VALUES(?, ?, ?)",
        [(i, int(y[i]), "dataset") for i in range(20)],
    )
    con.commit()
print(f"Base de datos de evidencia creada en: {db_path}")


print("\n=== 4. CONSTRUCCIÓN DE LA ONTOLOGÍA (GraphML) ===")
G = nx.DiGraph()

# Definición de conceptos y relaciones del dominio (mínimo 5 y 5)
G.add_edges_from([
    ("digito", "cero", {"rel": "tiene_clase"}),
    ("digito", "uno", {"rel": "tiene_clase"}),
    ("digito", "dos", {"rel": "tiene_clase"}),
    ("modelo_mlp", "digito", {"rel": "reconoce"}),
    ("imagen", "digito", {"rel": "representa"}),
    ("prediccion", "digito", {"rel": "asigna_clase"}),
    ("modelo_mlp", "prediccion", {"rel": "produce"}),
    ("sistema_hibrido", "modelo_mlp", {"rel": "integra"}),
    ("evidencia_sqlite", "imagen", {"rel": "almacena_metadatos"}),
    ("ontologia", "prediccion", {"rel": "interpreta_significado"})
])

# Enlace dinámico con una predicción
ejemplo_id = 15
clase_predicha = int(model.predict([X[ejemplo_id]])[0])
concepto_asignado = f"digito_{clase_predicha}"
G.add_edge(f"prediccion_{ejemplo_id}", concepto_asignado, rel="asigna_clase")
G.add_edge(f"imagen_{ejemplo_id}", f"prediccion_{ejemplo_id}", rel="genera_evidencia")

ontology_path = ARTIFACTS / "ontologia.graphml"
nx.write_graphml(G, ontology_path)
print(f"Ontología exportada con {G.number_of_edges()} relaciones en: {ontology_path}")
print(f"Ejemplo evaluado -> ID: {ejemplo_id} | Predicción: {clase_predicha} | Concepto: {concepto_asignado}")