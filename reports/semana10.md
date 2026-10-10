# Informe Técnico - Semana 10: Reconocimiento de Imágenes (Histogramas, Regiones y Texturas LBP)

## 1. Selección y Representación de Imágenes
* **Imagen 1 (`imagen_proyecto_1.png`):** Representa el estado base de los servidores y elementos tecnológicos del proyecto.
* **Imagen 2 (`imagen_proyecto_2.png`):** Representa una variante operativa con diferencias visuales y de iluminación en la infraestructura.
* **Objetivo:** Analizar y comparar las distribuciones de intensidad y texturas locales para validar la separación entre fondo y componentes[cite: 15].

---

## 2. Segmentación mediante Histogramas y Umbral de Otsu
* **Resultados:** El umbral automático de Otsu determinó valores de `0.6191` para la Imagen 1 y `0.6270` para la Imagen 2[cite: 15].
* **Interpretación:** La máscara binaria resultante aísla de manera limpia los gabinetes del fondo, permitiendo avanzar hacia el etiquetado geométrico de objetos[cite: 15].

---

## 3. Etiquetado y Medición de Regiones Conectadas
* **Métricas Obtenidas:** 
  * Se identificaron **6 regiones válidas** (superando el filtro de ruido de 50 píxeles).
  * **Área media:** 14,588.00 píxeles, con una desviación estándar de 3,2355.47, lo que refleja la variabilidad geométrica de los bloques detectados en la escena[cite: 15].

---

## 4. Análisis de Texturas LBP (Local Binary Pattern)
* **Comparativa:** Los histogramas LBP de patrones uniformes (de dimensión 18) muestran cómo se distribuyen las micro-estructuras y texturas superficiales de los equipos, permitiendo contrastar las diferencias espaciales entre ambas imágenes del proyecto[cite: 15].

---

## 5. Vector de Características Consolidado
* Se combinaron exitosamente las métricas de regiones, el histograma global de intensidad (32 bins) y el descriptor de texturas LBP, generando un vector unificado de **53 características** almacenado en `artifacts/semana10_features.npy`[cite: 15].

---

## 6. Limitaciones y Aplicación Futura
* **Limitaciones:** Cambios drásticos en la iluminación o sombras proyectadas pueden alterar los picos del histograma y desplazar el umbral de Otsu[cite: 15].
* **Aplicación Futura:** Alimentar modelos de Machine Learning para la clasificación automatizada de anomalías operativas en la infraestructura[cite: 15].