"""
Script Principal de Demostración - Semana 14
Autor: Daniel Eduardo Daza Cuello (ETITC - Ingeniería de Sistemas)
"""

from semana14_red_semantica import RedSemantica

def ejecutar_demostracion():
    print("=== INICIALIZACIÓN DE LA RED SEMÁNTICA (PROYECTO TI) ===")
    red = RedSemantica()

    oraciones = [
        "Un firewall es un dispositivo de red",
        "Un router es un dispositivo de red",
        "Un dispositivo de red es un activo de ti",
        "Un servidor es un activo de ti",
        "Un activo de ti requiere conexion segura"
    ]

    print("\n[PROCESANDO ORACIONES Y CONSTRUYENDO TRIPLES]")
    for oracion in oraciones:
        s, r, o = red.procesar_oracion(oracion)
        print(f"Hecho registrado: ({s}, {r}, {o})")

    print("\n=== CONSULTAS E INFERENCIAS ===")
    
    es_activo = red.es_un("firewall", "activo_ti")
    print(f"¿Firewall es un activo de TI? (Inferido): {es_activo}")

    req_firewall = red.consultar_propiedades("firewall")
    print(f"Requerimientos heredados para firewall: {req_firewall}")

    es_servidor_router = red.es_un("servidor", "router")
    print(f"¿Servidor es un router? (Sin evidencia): {es_servidor_router}")

    print("\n=== PRUEBA DE ENTRADA INVÁLIDA ===")
    try:
        red.procesar_oracion("Los enrutadores procesan paquetes velozmente")
    except ValueError as e:
        print(f"Excepción controlada correctamente: {e}")

if __name__ == "__main__":
    ejecutar_demostracion()