# Título:
# Auditoría con Tests Unitarios e Integración Web (40 puntos)

# Consigna:
# Previo a la puesta en producción, EcoTech Solutions debe certificar la precisión del algoritmo de cálculo de huella de carbono industrial. Tras auditar su comportamiento mediante pruebas automatizadas, dicho algoritmo debe integrarse en la tubería de datos que alimenta la interfaz web administrativa de la empresa.
# Punto A: Auditoría de Algoritmo de Emisiones ( unittest ): A partir de la función calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4) (la cual eleva ValueError si el consumo es negativo), implementa la clase de prueba TestCalculoEmisiones(unittest.TestCase). Diseña los casos de prueba necesarios para validar tanto la exactitud numérica del cálculo ante valores nominales como la correcta elevación de la excepción ante consumos fuera de rango.
# Punto B: Procesamiento de Métricas y Renderizado Web: Incorpora la función calcular_emisiones_carbono en la función obtener_metricas_consumo(registros), procesando un historial de consumos por planta industrial para determinar el total global de emisiones y la planta de mayor consumo. Por último, diseña la función de vista en Django vista_panel_sustentabilidad(request) que invoque dicho procesamiento y proporcione el diccionario de contexto listo para ser renderizado en la plantilla sustentabilidad/panel.html.







# Punto A: Auditoría de Algoritmo de Emisiones

#calculador de comsumos de carbono
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    
    # Validamos que el consumo no sea negativo
    if consumo_kwh < 0:
        raise ValueError("Has ingresado algo mal, me muerdo si el consumo en kWh es negativo amigo. ;-)")
    return consumo_kwh * factor_emision


# Punto B: Procesamiento de Métricas y Renderizado Web

def obtener_metricas_consumo(registros):
    total_emisiones = 0.0
    planta_mayor_consumo = "Ninguna"
    mayor_consumo_kwh = 0.0
    cantidad_plantas = 0

    for registro in registros:
        planta = registro.get("planta", "planta desconocida")
        consumo = registro.get("consumo_kwh", 0.0)

        # Calcula la emisión de esta planta y la suma al total global
        emision_planta = calcular_emisiones_carbono(consumo)
        total_emisiones += emision_planta

        # Compara para encontrar la planta que más consumió
        if consumo > mayor_consumo_kwh:
            mayor_consumo_kwh = consumo
            planta_mayor_consumo = planta

        # Cuenta cuántas plantas se procesaron
        cantidad_plantas += 1

    metricas = {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "mayor_consumo_kwh": mayor_consumo_kwh,
        "registros_procesados": cantidad_plantas,
    }

    return metricas


