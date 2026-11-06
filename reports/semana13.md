# Informe Técnico - Semana 13: Ingeniería del Conocimiento y Motor de Inferencia Lógica

## 1. Análisis Conceptual del Dominio
* **Problema Resuelto:** Automatización del diagnóstico de seguridad y despacho de alertas tempranas ante incidentes críticos de infraestructura en el proyecto de soporte TI.
* **Conceptos Controlados:** 
  * `alta_latencia_red`: Degradación anómala del canal de comunicaciones.
  * `fallo_autenticacion_api`: Anomalía en pasarela de acceso.
  * `amenaza_seguridad_detectada`: Conclusión intermedia sobre brecha potencial.
  * `alerta_incidente_despachada`: Meta final del sistema experto.

---

## 2. Reglas Lógicas Implementadas
Se diseñaron tres reglas Horn originales basadas en proposiciones e implicaciones ($P \land Q \to R$)[cite: 4]:
1. **R1_AlertaCritica:** $\text{alta\_latencia\_red} \land \text{fallo\_autenticacion\_api} \to \text{amenaza\_seguridad\_detectada}$[cite: 4]
2. **R2_ProtocoloDefensiva:** $\text{amenaza\_seguridad\_detectada} \land \text{firewall\_activo} \to \text{aislamiento\_segmento\_requerido}$[cite: 4]
3. **R3_NotificacionAutomatica:** $\text{aislamiento\_segmento\_requerido} \land \text{canal\_notificacion\_operativo} \to \text{alerta\_incidente\_despachada}$[cite: 4]

---

## 3. Pruebas Funcionales y Escenarios
* **Caso A (Conclusión Demostrada):** Provechando la totalidad de los hechos iniciales, el motor encadena de forma exitosa R1, R2 y R3, obteniendo como traza `['R1_AlertaCritica', 'R2_ProtocoloDefensiva', 'R3_NotificacionAutomatica']` y alcanzando la meta `alerta_incidente_despachada`[cite: 4].
* **Caso B (Conclusión No Demostrada):** Al omitir el hecho `canal_notificacion_operativo`, el motor ejecuta R1 y R2 de forma correcta, pero detiene su inferencia de manera elegante sin alcanzar la meta final[cite: 4]. 
  > **Nota conceptual importante:** Una conclusión *no demostrada* bajo lógica monótona y sistemas basados en reglas **no equivale a falsa**; simplemente significa que las evidencias aportadas en el caso actual son insuficientes para derivarla[cite: 4].

---

## 4. Resultados de las Pruebas Unitarias (`unittest`)
Se validó automatizadamente el comportamiento mediante `unittest`[cite: 4], comprobando:
1. Demostración exitosa en escenario completo[cite: 4].
2. Comportamiento correcto ante carencia de evidencias[cite: 4].
3. Inmutabilidad de los contenedores de datos de entrada[cite: 4].
4. Prevención absoluta de bucles infinitos ante dependencias circulares[cite: 4].

---

## 5. Limitaciones del Sistema
* El motor actual opera estrictamente bajo lógica proposicional positiva sin soporte para factores de certeza (incertidumbre) ni cuantificadores de primer orden[cite: 4].