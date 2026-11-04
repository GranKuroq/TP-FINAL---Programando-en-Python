# Título:
# Sanitización y Análisis Estadístico de Sensores (20 puntos)

# Consigna:
# Los microcontroladores de EcoTech Solutions transmiten lecturas térmicas en formato heterogéneo con espacios indeseados, textos mezclados con unidades de medida y atributos incompletos. Se necesita un componente que normalice estos registros individuales y genere un reporte consolidado para la toma de decisiones.
# Punto A: Normalización de Lecturas ( limpiar_registro_sensor ): Diseña la función limpiar_registro_sensor(registro_raw) encargada de procesar un diccionario con datos crudos de un sensor (por ejemplo: {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}). La función debe transformar la información para retornar un nuevo diccionario estandarizado, garantizando que el identificador quede sin espacios sobrantes, la temperatura sea un valor numérico de tipo float sin sufijos de unidad, y la ubicación posea un valor por defecto seguro en caso de no haberse registrado.
# Punto B: Monitoreo y Mapeo Estadístico ( generar_resumen_sensores ): Desarrolla la función generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura) que tome una colección de registros sanitizados previamente con la función del Punto A y un valor límite. Debe retornar una tupla (lista_sensores_alerta, promedio_temperatura) conteniendo los IDs de los dispositivos que superan el umbral estipulado y el promedio térmico global de la planta. Incluye un bloque de ejecución que demuestre el flujo completo desde la limpieza de registros crudos hasta la impresión formateada del reporte final.


# Punto A: Normalización de Lecturas
def limpiar_registro_sensor(registro_raw: dict[str, str]):
    
    sensor_id = (registro_raw.get("sensor_id")).strip()

    temp_str = str(registro_raw.get("temperatura", "0.0")).strip()
    temp_limpia = temp_str.upper().replace("°C", "").replace("C", "").replace("°", "").strip()
    try:
        temperatura = float(temp_limpia)
    except ValueError:
        print(f"Aviso: Valor de temperatura inválido en {sensor_id}, se asigna 0.0 °C por defecto.")
        temperatura = 0.0

    ubicacion = str(registro_raw.get("ubicacion", "")).strip()
    if ubicacion == "":
        ubicacion = "Ubicacion Desconocida"

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }

    return registro_limpio


# umbral térmico por defecto (decidi ampliar a un rango de mins y maxs, con una posibilidad de seteo por parte del usuario)
umbral_min = 22.0
umbral_max = 30.0


# Punto B: Monitoreo y Mapeo Estadístico
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura=(umbral_min, umbral_max)):
    
    min_temp, max_temp = umbral_temperatura
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    
    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        if temperatura < min_temp or temperatura > max_temp:
            lista_sensores_alerta.append(sensor["sensor_id"])
        suma_temperaturas += temperatura

    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
        return (lista_sensores_alerta, promedio_temperatura)
    else:
        return ([], 0.0)
     

# Bloque Principal

# Datos de prueba
datos_raw = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002  ", "temperatura": " 31.2°C ", "ubicacion": "Planta Sur"},
        {"sensor_id": "  SENSOR-003", "temperatura": "28.0 C"},
        {"sensor_id": " SENSOR-004 ", "temperatura": "35.8c", "ubicacion": "   "},
        {"sensor_id": "SENSOR-005", "temperatura": "18.5C", "ubicacion": "Ala Sucutrildad"},
        {"sensor_id": "SENSOR-006", "temperatura": "21.5C", "ubicacion": "Sector Almacén"},
        {"sensor_id": "SENSOR-007", "temperatura": "25.5C", "ubicacion": "Planta Este"},
        {"sensor_id": "SENSOR-008", "temperatura": "11.4C", "ubicacion": "Sala de Cómputos"},
        {"sensor_id": "SENSOR-009", "temperatura": "11.5C", "ubicacion": "Casa de Huéspedes"},
        {"sensor_id": "SENSOR-010", "temperatura": "31.5C", "ubicacion": "Sector Ea Ea Pepé"},
    ]


if __name__ == "__main__":

    print("=" * 60)
    print("   CONFIGURACIÓN DE UMBRAL TÉRMICO - ECOTECH SOLUTIONS")
    print("=" * 60)
    print(f"Umbral actual configurado -> Mínima: {umbral_min} °C | Máxima: {umbral_max} °C")

    respuesta = input("¿Desea cambiar estos valores de umbral? (si/no): ").strip().lower()
    if respuesta in ("si", "sí", "s"):
        try:
            entrada_min = str(input("  Ingrese el nuevo valor de temperatura mínima (°C): ")).strip()
            nuevo_min = float(entrada_min)
            entrada_max = str(input("  Ingrese el nuevo valor de temperatura máxima (°C): ")).strip()
            nuevo_max = float(entrada_max)
            umbral_min = nuevo_min
            umbral_max = nuevo_max
            print(f"Nuevo umbral establecido  -> Mínima: {umbral_min} °C | Máxima: {umbral_max} °C")
        except ValueError:
            print(
                "Error: El valor ingresado no es un número válido (float). "
                f"Se mantienen los valores por defecto ({umbral_min} °C a {umbral_max} °C)."
            )

    umbral_temperatura = (umbral_min, umbral_max)

    registros_limpios = []
    for registro in datos_raw:
        registro_limpio = limpiar_registro_sensor(registro)
        registros_limpios.append(registro_limpio)

    sensores_alerta, promedio_planta = generar_resumen_sensores(registros_limpios, umbral_temperatura)

    print("\n" + "=" * 60)
    print("   REPORTE CONSOLIDADO DE SENSORES - ECOTECH SOLUTIONS")
    print("=" * 60)
    print("\n[1] REGISTROS SANITIZADOS:")
    for reg in registros_limpios:
        print(
            f"  • ID: {reg['sensor_id']:<12} | "
            f"Temp: {reg['temperatura']:>5.1f} °C | "
            f"Ubicación: {reg['ubicacion']}"
        )

    print("\n[2] RESUMEN ESTADÍSTICO Y ALERTAS:")
    print("=" * 60)
    print(f"  • Sensores analizados          : {len(registros_limpios)}")
    print(f"  • Promedio térmico global      : {promedio_planta:.2f} °C")
    print(f"  • Rango de umbral configurado  : {umbral_min:.1f} °C a {umbral_max:.1f} °C")

    if len(sensores_alerta) > 0:
        print("  • Sensores en alerta (fuera de rango):")
        for sensor_id in sensores_alerta:
            print(f"      - {sensor_id}")
    else:
        print("  • Sensores en alerta (fuera de rango): Ninguno")

    print("=" * 60)
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




