"""
Módulo de Reconocimiento de Imágenes - Semana 09
Procesamiento de imágenes: características, contornos (Canny), 
segmentación (Otsu) y análisis de regiones conectadas.
"""

from pathlib import Path
import matplotlib
# Configurar backend no interactivo para evitar errores de Tkinter en Windows
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from skimage import color, feature, filters, img_as_float, io, measure

# Configuración de directorios de trabajo
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
ARTIFACTS_DIR = ROOT / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Selección y carga de la imagen del proyecto
image_path = DATA_DIR / "imagen_proyecto.png"
if image_path.exists():
    raw_image = io.imread(image_path)
    if raw_image.ndim == 3:
        image = color.rgb2gray(raw_image)
    else:
        image = img_as_float(raw_image)
    print(f"[INFO] Imagen cargada desde {image_path}")
else:
    from skimage import data
    image = data.coins()
    print("[INFO] Usando imagen de respaldo integrada para demostración.")

print("=== 1. EXTRACCIÓN DE CARACTERÍSTICAS BÁSICAS ===")
print(f"Dimensiones de la matriz (Alto x Ancho): {image.shape}")
print(f"Intensidad mínima: {image.min():.4f} | Intensidad máxima: {image.max():.4f}")

print("\n=== 2. DETECCIÓN DE CONTORNOS (Filtro Canny) ===")
# Normalizamos la imagen a rango [0, 1] si está en formato de 0-255
image_norm = image / 255.0 if image.max() > 1.0 else image
sigma_val = 2.0
edges = feature.canny(image_norm, sigma=sigma_val)
print(f"Contornos detectados con sigma={sigma_val}")

print("\n=== 3. SEGMENTACIÓN MEDIANTE UMBRAL AUTOMÁTICO (Otsu) ===")
thresh = filters.threshold_otsu(image)
mask = image > thresh
print(f"Umbral Otsu obtenido: {thresh:.4f}")

print("\n=== 4. ANÁLISIS DE REGIONES CONECTADAS ===")
label_image = measure.label(mask)
num_regions = label_image.max()
print(f"Número de regiones conectadas identificadas: {num_regions}")

print("\n=== 5. GENERACIÓN DE EVIDENCIA VISUAL ===")
fig, axes = plt.subplots(1, 3, figsize=(14, 5))

axes[0].imshow(image, cmap="gray")
axes[0].set_title("1. Imagen Original")

axes[1].imshow(edges, cmap="gray")
axes[1].set_title(f"2. Contornos Canny (sigma={sigma_val})")

axes[2].imshow(mask, cmap="gray")
axes[2].set_title(f"3. Máscara Otsu (Umbral: {thresh:.2f})")

for ax in axes:
    ax.axis("off")

fig.tight_layout()
output_image_path = ARTIFACTS_DIR / "semana09_vision.png"
fig.savefig(output_image_path, dpi=160)
print(f"Evidencia visual guardada exitosamente en: {output_image_path}")
plt.close(fig)