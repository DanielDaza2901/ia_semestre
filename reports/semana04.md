# Informe Técnico - Semana 04: Marco Tecnológico de la Inteligencia Artificial

## 1. Introducción
Este informe documenta la formalización de problemas mediante espacios de estados, la implementación de búsqueda informada utilizando el algoritmo $A^*$ con heurística de distancia Manhattan, y la toma de decisiones en entornos adversariales con el algoritmo Minimax optimizado mediante poda alfa-beta.

---

## 2. Formulación y Componentes de Búsqueda ($A^*$)
En el script `src/semana04_astar.py`, el problema de navegación se estructura bajo los siguientes componentes formales:
* **Estado:** Coordenada en formato tupla $(fila, columna)$ que representa la posición actual en la cuadrícula `GRID`.
* **Acción:** Movimientos permitidos en las cuatro direcciones cardinales (arriba, abajo, izquierda, derecha).
* **Transición:** Desplazamiento desde un nodo actual a una celda vecina válida que no contenga barreras u obstáculos (`#`).
* **Meta (`GOAL`):** Casilla destino ubicada en la coordenada `(4, 4)`.
* **Costo de camino ($g(n)$):** Cada paso ortogonal posee un costo uniforme de `1`.
* **Heurística ($h(n)$):** Distancia Manhattan ($|r_1 - r_2| + |c_1 - c_2|$), la cual es admisible y consistente al no sobreestimar el costo real en una cuadrícula ortogonal.

---

## 3. Formulación y Componentes de Juegos Adversariales (Minimax)
En el script `src/semana04_minimax.py`, el entorno competitivo de tres en línea se define mediante:
* **Estado de juego:** Configuración actual de las 9 casillas del tablero.
* **Acción:** Colocación de una marca legal en una casilla vacía (" ").
* **Jugador MAX (`"X"`):** Agente que busca maximizar la utilidad del resultado.
* **Jugador MIN (`"O"`):** Agente racional que intenta minimizar la utilidad del oponente.
* **Estados Terminales y Utilidad:** Victoria de X (`+1`), Victoria de O (`-1`), o Empate / Tablero lleno (`0`).
* **Decisión:** Selección de la jugada óptima anticipando que el adversario responderá de forma ideal.

---

## 4. Mejoras y Optimizaciones implementadas

Con el fin de elevar el rigor técnico, la auditabilidad y la eficiencia de los scripts, se incorporaron dos mejoras fundamentales:

### A. Renderizado Gráfico de Cuadrícula (`semana04_astar.py`)
* **¿Por qué se hizo?:** Las coordenadas puras en texto (tuplas) dificultan la verificación rápida del comportamiento espacial del algoritmo frente a los obstáculos.
* **¿Para qué sirve?:** Permite realizar una auditoría visual directa en la consola imprimiendo el mapa con asteriscos (`*`) para el camino y almohadillas (`#`) para las barreras, garantizando de inmediato que la ruta sea continua y válida.

### B. Implementación de Poda Alfa-Beta ($\alpha$-$\beta$ Pruning) en Minimax (`semana04_minimax.py`)
* **¿Por qué se hizo?:** El algoritmo Minimax clásico evalúa exhaustivamente todas las ramas del árbol de decisiones, lo que incrementa innecesariamente el costo computacional a medida que crece la profundidad.
* **¿Para qué sirve?:** Introduce los parámetros de acotamiento $\alpha$ (mejor opción garantizada para MAX) y $\beta$ (mejor opción garantizada para MIN). Al cumplirse la condición $\beta \le \alpha$, el algoritmo descarta (*poda*) subárboles completos que no alterarán la decisión óptima final. Esto reduce drásticamente el tiempo de procesamiento sin perder la garantía de optimalidad del resultado.

---

## 5. Conclusiones
* La combinación de $f(n) = g(n) + h(n)$ en $A^*$ permite priorizar estados prometedores eficientemente, evitando la exploración innecesaria propia de métodos no informados.
* La optimización con poda alfa-beta demuestra cómo equilibrar la profundidad analítica y la eficiencia temporal en la toma de decisiones de agentes en entornos adversariales.