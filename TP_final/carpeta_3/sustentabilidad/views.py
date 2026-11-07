from django.shortcuts import render

from .services import calcular_emisiones_carbono, obtener_metricas_consumo

def vista_panel_sustentabilidad(request):
    
    # Historial de consumos de las plantas
    historial_consumos = [
        {"planta": "Planta Sucutrule", "consumo_kwh": 1200.0},
        {"planta": "Planta EaPePé", "consumo_kwh": 1850.5},
        {"planta": "Planta BlackTuple", "consumo_kwh": 950.0},
        {"planta": "Planta Pipi Cucú", "consumo_kwh": 620.0},
    ]

    # Ampliamos cada registro con su emisión individual para mostrarla
    for registro in historial_consumos:
        registro["emision_co2"] = calcular_emisiones_carbono(registro["consumo_kwh"])

    # Obtiene el diccionario con los resultados
    resultado_metricas = obtener_metricas_consumo(historial_consumos)

    # Crea el diccionario para enviarlo al archivo HTML
    contexto = {
        "empresa": "EcoTech Solutions",
        "total_emisiones": resultado_metricas["total_emisiones"],
        "planta_mayor_consumo": resultado_metricas["planta_mayor_consumo"],
        "mayor_consumo_kwh": resultado_metricas["mayor_consumo_kwh"],
        "registros_procesados": resultado_metricas["registros_procesados"],
        "registros": historial_consumos,
    }

    return render(request, "sustentabilidad/panel.html", contexto)