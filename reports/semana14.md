# Informe Técnico - Semana 14: Ingeniería del Conocimiento y Redes Semánticas

## 1. Modelado del Dominio (Infraestructura TI)
* **Conceptos Seleccionados (Nodos):** 
  * `firewall`
  * `router`
  * `dispositivo_de_red`
  * `servidor`
  * `activo_de_ti`
  * `conexion_segura`
* **Relaciones Definidas (Aristas):**
  * `es_un`: Relación taxonómica jerárquica con soporte para transitividad.
  * `requiere`: Relación de asociación y herencia de propiedades o requerimientos técnicos.

---

## 2. Interpretación Lingüística y Triples Explícitos
El sistema procesó oraciones en lenguaje natural mediante un analizador sintáctico basado en patrones regulares fijos, aplicando normalización canónica (conversión a minúsculas con `casefold` y eliminación de tildes mediante Unicode `NFD`):
1. `(firewall, es_un, dispositivo_de_red)`
2. `(router, es_un, dispositivo_de_red)`
3. `(dispositivo_de_red, es_un, activo_de_ti)`
4. `(servidor, es_un, activo_de_ti)`
5. `(activo_de_ti, requiere, conexion_segura)`

---

## 3. Inferencia por Jerarquía y Herencia de Propiedades
* **Transitividad (`es_un`):** El motor recorre el grafo de conceptos ascendentes utilizando una pila de pendientes y un conjunto de control de ciclos (`visitados`) para garantizar robustez.
* **Herencia de Propiedades (`requiere`):** Permite propagar atributos desde las clases superiores o categorías base hacia los nodos hijos de la jerarquía.
* **Manejo de Excepciones:** Las oraciones que no coinciden con los patrones gramaticales programados lanzan de forma controlada un `ValueError`.

---

## 4. Resultados de la Ejecución y Pruebas Unitarias
La ejecución del script principal y la validación mediante pruebas automatizadas con `unittest` demostraron:
* Registro correcto de los triples explícitos en la estructura de red.
* Funcionamiento exitoso de la herencia de propiedades (heredando correctamente `conexion_segura` para los componentes de la infraestructura).
* Control estricto de entradas inválidas y oraciones no admitidas por el analizador sintáctico.