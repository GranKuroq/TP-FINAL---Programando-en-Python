# Título:
# Auditoría con Tests Unitarios e Integración Web (40 puntos)

# Consigna:
# Previo a la puesta en producción, EcoTech Solutions debe certificar la precisión del algoritmo de cálculo de huella de carbono industrial. Tras auditar su comportamiento mediante pruebas automatizadas, dicho algoritmo debe integrarse en la tubería de datos que alimenta la interfaz web administrativa de la empresa.
# Punto A: Auditoría de Algoritmo de Emisiones ( unittest ): A partir de la función calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4) (la cual eleva ValueError si el consumo es negativo), implementa la clase de prueba TestCalculoEmisiones(unittest.TestCase). Diseña los casos de prueba necesarios para validar tanto la exactitud numérica del cálculo ante valores nominales como la correcta elevación de la excepción ante consumos fuera de rango.
# Punto B: Procesamiento de Métricas y Renderizado Web: Incorpora la función calcular_emisiones_carbono en la función obtener_metricas_consumo(registros), procesando un historial de consumos por planta industrial para determinar el total global de emisiones y la planta de mayor consumo. Por último, diseña la función de vista en Django vista_panel_sustentabilidad(request) que invoque dicho procesamiento y proporcione el diccionario de contexto listo para ser renderizado en la plantilla sustentabilidad/panel.html.

import unittest


# Punto A: Auditoría de Algoritmo de Emisiones ( unittest )

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    # Validamos que el consumo no sea negativo
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")

    # Multiplicamos el consumo por el factor de emisión
    emisiones = consumo_kwh * factor_emision
    emisiones_redondeadas = round(emisiones, 2)
    return emisiones_redondeadas


class TestCalculoEmisiones(unittest.TestCase):

    # Caso 1: Prueba con un valor normal usando el factor por defecto (0.4)
    def test_calculo_valor_nominal(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40.0)

    # Caso 2: Prueba cuando el consumo es 0
    def test_calculo_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0.0)

    # Caso 3: Prueba indicando otro factor de emisión distinto al por defecto
    def test_calculo_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(250, 0.5)
        self.assertEqual(resultado, 125.0)

    # Caso 4: Prueba que verifica que un número negativo lance ValueError
    def test_consumo_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)


# Punto B: Procesamiento de Métricas y Renderizado Web

def obtener_metricas_consumo(registros):
    total_emisiones = 0.0
    planta_mayor_consumo = "Ninguna"
    mayor_consumo_kwh = 0.0
    cantidad_plantas = 0

    for registro in registros:
        nombre_planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        # 1. Calculamos la emisión de esta planta y la sumamos al total global
        emision_planta = calcular_emisiones_carbono(consumo)
        total_emisiones = total_emisiones + emision_planta

        # 2. Comparamos para encontrar la planta que más consumió
        if consumo > mayor_consumo_kwh:
            mayor_consumo_kwh = consumo
            planta_mayor_consumo = nombre_planta

        # 3. Contamos cuántas plantas se procesaron
        cantidad_plantas = cantidad_plantas + 1

    total_emisiones = round(total_emisiones, 2)

    metricas = {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "mayor_consumo_kwh": mayor_consumo_kwh,
        "registros_procesados": cantidad_plantas,
    }

    return metricas


def vista_panel_sustentabilidad(request):
    from django.shortcuts import render

    # Lista de consumos de las plantas industriales de EcoTech Solutions
    historial_consumos = [
        {"planta": "Planta Norte", "consumo_kwh": 1200.0},
        {"planta": "Planta Sur", "consumo_kwh": 1850.5},
        {"planta": "Planta Este", "consumo_kwh": 950.0},
        {"planta": "Sector Almacén", "consumo_kwh": 620.0},
    ]

    # Obtenemos el diccionario con los resultados procesados
    resultado_metricas = obtener_metricas_consumo(historial_consumos)

    # Armamos el diccionario de contexto para enviarlo al archivo HTML
    contexto = {
        "empresa": "EcoTech Solutions",
        "total_emisiones": resultado_metricas["total_emisiones"],
        "planta_mayor_consumo": resultado_metricas["planta_mayor_consumo"],
        "mayor_consumo_kwh": resultado_metricas["mayor_consumo_kwh"],
        "registros": historial_consumos,
    }

    return render(request, "sustentabilidad/panel.html", contexto)


# Bloque Principal de Prueba
if __name__ == "__main__":
    print("=" * 65)
    print("   AUDITORÍA DE EMISIONES Y MÉTRICAS WEB - ECOTECH SOLUTIONS")
    print("=" * 65)

    # 1. Demostración de procesamiento de métricas (Punto B)
    datos_prueba = [
        {"planta": "Planta Norte", "consumo_kwh": 1200.0},
        {"planta": "Planta Sur", "consumo_kwh": 1850.5},
        {"planta": "Planta Este", "consumo_kwh": 950.0},
        {"planta": "Sector Almacén", "consumo_kwh": 620.0},
    ]

    resumen = obtener_metricas_consumo(datos_prueba)

    print("\n[1] RESULTADO DE MÉTRICAS DE CONSUMO Y EMISIONES:")
    print(f"  • Plantas evaluadas         : {resumen['registros_procesados']}")
    print(f"  • Total global de emisiones : {resumen['total_emisiones']} kg CO2")
    print(f"  • Planta de mayor consumo   : {resumen['planta_mayor_consumo']} ({resumen['mayor_consumo_kwh']} kWh)")

    # 2. Ejecución de los tests unitarios (Punto A)
    print("\n[2] EJECUTANDO AUDITORÍA DE TESTS UNITARIOS (unittest):")
    print("-" * 65)
    unittest.main(verbosity=2, exit=False)
    print(" Developed By: Sucutrule Productions          8-)")
    print("""
______██████████████
-____██▓▓▓▓▓▓▓▓▓ M ▓████
-__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
-__██████░░░░██░░██████
██░░░░████░░██░░░░░░░░██
██░░░░████░░░░██░░░░░░██
-__████░░░░░░██████████
-__██░░░░░░░░░░░░░██
_____██░░░░░░░░░██
-______██░░░░░░██
-____██▓▓████▓▓▓█
-_██▓▓▓▓▓▓████▓▓█
██▓▓▓▓▓▓███░░███░
-__██░░░░░░███████
-____██░░░░███████
-______██████████
-_____██▓▓▓▓▓▓▓▓▓██
-_____█████████████
""")
