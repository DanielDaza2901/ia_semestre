"""
Módulo de Reconocimiento de Imágenes: Histogramas, Regiones y Texturas LBP - Semana 10
Autor: Daniel Eduardo Daza Cuello (ETITC - Ingeniería de Sistemas)
"""

from pathlib import Path
import matplotlib
# Configurar backend no interactivo para evitar errores de GUI en Windows
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from skimage import color, data, filters, img_as_float, io, measure
from skimage.feature import local_binary_pattern

# Configuración de directorios de trabajo
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
ARTIFACTS_DIR = ROOT / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

def procesar_imagen_proyecto(ruta_img1, ruta_img2):
    print("=== 1. SELECCIÓN Y CARGA DE IMÁGENES DEL PROYECTO ===")
    
    # Carga de la Imagen 1
    if ruta_img1.exists():
        raw1 = io.imread(ruta_img1)
        img1 = color.rgb2gray(raw1) if raw1.ndim == 3 else img_as_float(raw1)
        print(f"[INFO] Imagen 1 cargada: {ruta_img1.name} | Dimensiones: {img1.shape}")
    else:
        img1 = data.coins()
        print("[INFO] Usando imagen de respaldo 1 (coins).")

    # Carga de la Imagen 2
    if ruta_img2.exists():
        raw2 = io.imread(ruta_img2)
        img2 = color.rgb2gray(raw2) if raw2.ndim == 3 else img_as_float(raw2)
        print(f"[INFO] Imagen 2 cargada: {ruta_img2.name} | Dimensiones: {img2.shape}")
    else:
        img2 = data.brick()
        print("[INFO] Usando imagen de respaldo 2 (brick).")

    print("\n=== 2. SEGMENTACIÓN MEDIANTE UMBRAL AUTOMÁTICO (Otsu) ===")
    # Asegurar rango [0, 1] o escala adecuada
    img1_norm = img1 / 255.0 if img1.max() > 1.0 else img1
    img2_norm = img2 / 255.0 if img2.max() > 1.0 else img2

    thresh1 = filters.threshold_otsu(img1_norm)
    mask1 = img1_norm > thresh1
    
    thresh2 = filters.threshold_otsu(img2_norm)
    mask2 = img2_norm > thresh2
    
    print(f"Umbral Otsu - Imagen 1: {thresh1:.4f} | Imagen 2: {thresh2:.4f}")

    print("\n=== 3. ETIQUETADO Y MEDICIÓN DE REGIONES (Conectadas) ===")
    labels1 = measure.label(mask1)
    # Filtrar regiones con área mayor a 50 píxeles para eliminar ruido
    regions1 = [r for r in measure.regionprops(labels1) if r.area > 50]
    areas1 = np.array([r.area for r in regions1], dtype=float)
    
    area_mean1 = float(areas1.mean()) if len(areas1) else 0.0
    area_std1 = float(areas1.std()) if len(areas1) else 0.0
    
    print(f"Regiones válidas (>50px) en Img 1: {len(regions1)} | Área Media: {area_mean1:.2f} | Desviación: {area_std1:.2f}")

    print("\n=== 4. EXTRACCIÓN DE HISTOGRAMAS Y TEXTURAS LBP ===")
    # Histograma de intensidad global (32 bins, normalizado)
    hist_int1, _ = np.histogram(img1_norm.ravel(), bins=32, range=(0, 1), density=True)
    
    # Análisis de texturas con Local Binary Pattern (LBP)
    radius = 2
    points = 8 * radius
    lbp1 = local_binary_pattern(img1_norm, points, radius, method="uniform")
    hist_lbp1, _ = np.histogram(lbp1.ravel(), bins=np.arange(0, points + 3), density=True)

    # Histograma para Imagen 2 (para contraste y comparación)
    hist_int2, _ = np.histogram(img2_norm.ravel(), bins=32, range=(0, 1), density=True)
    lbp2 = local_binary_pattern(img2_norm, points, radius, method="uniform")
    hist_lbp2, _ = np.histogram(lbp2.ravel(), bins=np.arange(0, points + 3), density=True)

    print(f"Dimensión descriptor LBP: {len(hist_lbp1)}")

    print("\n=== 5. CONSOLIDACIÓN DEL VECTOR DE CARACTERÍSTICAS (.npy) ===")
    # Combinar métricas de regiones, histograma de intensidad y texturas LBP
    feature_vector = np.concatenate([
        [area_mean1, area_std1, len(regions1)],
        hist_int1,
        hist_lbp1
    ])
    
    npy_path = ARTIFACTS_DIR / "semana10_features.npy"
    np.save(npy_path, feature_vector)
    print(f"Vector de características guardado exitosamente en: {npy_path} (Dimensión total: {len(feature_vector)})")

    print("\n=== 6. GENERACIÓN DE EVIDENCIA VISUAL (Histogramas) ===")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].plot(hist_int1, color='blue', label='Img 1 (Intensidad)')
    axes[0].plot(hist_int2, color='orange', label='Img 2 (Intensidad)')
    axes[0].set_title("Comparativa de Histogramas de Intensidad")
    axes[0].set_xlabel("Bins")
    axes[0].set_ylabel("Densidad normalizada")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(hist_lbp1, color='green', label='Img 1 (LBP Textura)')
    axes[1].plot(hist_lbp2, color='purple', label='Img 2 (LBP Textura)')
    axes[1].set_title("Comparativa de Histogramas LBP (Texturas)")
    axes[1].set_xlabel("Patrones LBP Uniformes")
    axes[1].set_ylabel("Densidad normalizada")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    img_output_path = ARTIFACTS_DIR / "semana10_histograma.png"
    fig.savefig(img_output_path, dpi=160)
    print(f"Gráfica de histogramas guardada en: {img_output_path}")
    plt.close(fig)

if __name__ == "__main__":
    img_p1 = DATA_DIR / "imagen_proyecto_1.png"
    img_p2 = DATA_DIR / "imagen_proyecto_2.png"
    procesar_imagen_proyecto(img_p1, img_p2)