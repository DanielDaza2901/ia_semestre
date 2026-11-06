"""
Módulo de Redes Semánticas e Inferencia por Jerarquía - Semana 14
Autor: Daniel Eduardo Daza Cuello (ETITC - Ingeniería de Sistemas)
Propósito: Modelar conceptos de TI, interpretar oraciones, almacenar triples y ejecutar
inferencias por transitividad y herencia de propiedades.
"""

import re
import unicodedata
from typing import List, Set, Tuple

def normalizar(texto: str) -> str:
    """
    Normaliza una cadena de texto eliminando tildes, espacios adicionales
    y convirtiéndola a minúsculas canónicas (casefold + NFD).
    """
    if not isinstance(texto, str):
        return ""
    base = unicodedata.normalize("NFD", texto.casefold().strip())
    limpio = "".join(c for c in base if unicodedata.category(c) != "Mn")
    return re.sub(r'\s+', '_', limpio)


class RedSemantica:
    """Implementa una red semántica dirigida con soporte para triples, jerarquías e inferencia."""

    def __init__(self):
        self.aristas: dict[str, List[Tuple[str, str]]] = {}
        self.triples: Set[Tuple[str, str, str]] = set()

    def agregar_triple(self, sujeto: str, relacion: str, objeto: str) -> None:
        """Agrega un triple explícito a la red semántica."""
        s = normalizar(sujeto)
        r = normalizar(relacion)
        o = normalizar(objeto)

        if not s or not r or not o:
            raise ValueError("Los elementos del triple no pueden estar vacíos.")

        triple = (s, r, o)
        if triple not in self.triples:
            self.triples.add(triple)
            if s not in self.aristas:
                self.aristas[s] = []
            self.aristas[s].append((r, o))

    def interpretar_oracion(self, oracion: str) -> Tuple[str, str, str]:
        """
        Interpreta oraciones simples del dominio mediante patrones lingüísticos fijos:
        - Patrón 1: "Un [sujeto] es un [objeto]" -> relación 'es_un'
        - Patrón 2: "[sujeto] requiere [objeto]" -> relación 'requiere'
        """
        texto = oracion.strip().lower()
        texto_limpio = re.sub(r'^(un|una|el|la)\s+', '', texto)

        match_es = re.match(r'^(.+?)\s+es\s+u[nn]a?\s+(.+?)\.?$', texto_limpio)
        if match_es:
            sujeto = normalizar(match_es.group(1))
            objeto = normalizar(match_es.group(2))
            return (sujeto, "es_un", objeto)

        match_req = re.match(r'^(.+?)\s+requiere\s+(.+?)\.?$', texto_limpio)
        if match_req:
            sujeto = normalizar(match_req.group(1))
            objeto = normalizar(match_req.group(2))
            return (sujeto, "requiere", objeto)

        raise ValueError(f"Oración no admitida por el analizador sintáctico: '{oracion}'")

    def procesar_oracion(self, oracion: str) -> Tuple[str, str, str]:
        """Interpreta una oración y la registra automáticamente en la red."""
        s, r, o = self.interpretar_oracion(oracion)
        self.agregar_triple(s, r, o)
        return (s, r, o)

    def es_un(self, origen: str, categoria: str) -> bool:
        """
        Calcula por transitividad si el concepto 'origen' pertenece a 'categoria'
        siguiendo las aristas 'es_un', utilizando control de ciclos con 'visitados'.
        """
        orig = normalizar(origen)
        cat = normalizar(categoria)

        pendientes = [orig]
        visitados = set()

        while pendientes:
            actual = pendientes.pop()
            if actual == cat:
                return True
            if actual in visitados:
                continue
            visitados.add(actual)

            for relacion, destino in self.aristas.get(actual, []):
                if relacion == "es_un":
                    pendientes.append(destino)

        return False

    def consultar_propiedades(self, concepto: str) -> List[str]:
        """
        Realiza herencia de propiedades (relación 'requiere') recorriendo
        la jerarquía ascendente de la categoría ('es_un').
        """
        c = normalizar(concepto)
        propiedades = set()

        ancestros = {c}
        pendientes = [c]
        visitados = set()

        while pendientes:
            actual = pendientes.pop()
            if actual in visitados:
                continue
            visitados.add(actual)
            ancestros.add(actual)

            for relacion, destino in self.aristas.get(actual, []):
                if relacion == "es_un":
                    pendientes.append(destino)

        for nodo in ancestros:
            for relacion, destino in self.aristas.get(nodo, []):
                if relacion == "requiere":
                    propiedades.add(destino)

        return sorted(list(propiedades))