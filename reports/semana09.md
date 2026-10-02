# Informe Técnico - Semana 09: Reconocimiento de Imágenes y Visión Artificial

## 1. Imagen Utilizada y Relación con el Proyecto
* **Representación:** La imagen (`data/imagen_proyecto.png`) representa servidores informáticos del dominio del proyecto, los cuales muestran diferentes estados operativos (normales frente a sobrecalentados o con fallas).
* **Utilidad:** Permite transformar una representación gráfica bidimensional en una matriz numérica de intensidades para extraer métricas estructurales previas a la clasificación automatizada de alertas operativas.
* **Información esperada:** Aislar los bordes perimetrales de los gabinetes de servidores y segmentar las regiones de interés separándolas del fondo blanco.

---

## 2. Resultado de Detección de Contornos (Canny)
* **Efecto visual:** El operador de Canny resalta con alta precisión los cambios abruptos de intensidad en la matriz de píxeles, delimitando los contornos exteriores de los servidores y los detalles de las rejillas de ventilación.
* **Impacto del parámetro Sigma:** 
  * Un **sigma bajo** preserva líneas y detalles finos (como el humo o las sombras), pero introduce ruido.
  * Un **sigma alto** (`sigma=2.0`) suaviza la imagen de forma gaussiana, eliminando el ruido superficial y consolidando los bordes principales de los equipos.

---

## 3. Umbral Otsu Obtenido
* **Valor calculado:** El algoritmo de Otsu determinó de forma automática un umbral de `0.6191` a partir del análisis del histograma de intensidades.
* **Interpretación de la máscara binaria:** La segmentación separa de manera limpia los gabinetes oscuros del fondo claro, generando una matriz booleana óptima para la identificación de objetos.

---

## 4. Número de Regiones Encontradas
* El etiquetado de componentes conexos sobre la máscara binaria identificó **11 regiones conectadas**.
* Estas regiones corresponden a los distintos bloques de los servidores, indicadores visuales de estado y elementos de texto/marcas de agua detectados de forma independiente.

---

## 5. Limitaciones Encontradas
* Presencia de marcas de agua o textos en la parte inferior que generan regiones conectadas adicionales no deseadas.
* Sensibilidad a variaciones de contraste en zonas oscuras del equipo que pueden fragmentar un componente único en múltiples regiones.

---

## 6. Aplicación Futura dentro del Proyecto
* Las máscaras binarias y contornos extraídos servirán como vectores de características de entrada para alimentar modelos de clasificación o sistemas expertos que automaticen la detección temprana de anomalías en la infraestructura tecnológica del proyecto.