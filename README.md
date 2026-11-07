# 🌱 EcoTech Solutions — Panel de Sustentabilidad y Auditoría de Emisiones

Proyecto web desarrollado en **Python** y **Django** para **EcoTech Solutions**, orientado a certificar y visualizar el cálculo de la huella de carbono industrial de sus plantas operativas mediante pruebas unitarias automatizadas (`unittest`) y un panel administrativo web.

---

## 📋 Descripción General

El sistema consta de dos módulos principales integrados dentro de la aplicación `sustentabilidad`:

1. **Auditoría del Algoritmo de Emisiones (`unittest`):**
   - Función `calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4)` que calcula las emisiones de $\text{CO}_2$ en kilogramos y valida que el consumo eléctrico no sea negativo (elevando `ValueError` en caso de valores fuera de rango).
   - Suite de pruebas unitarias `TestCalculoEmisiones(unittest.TestCase)` que certifica cálculos con valores nominales, consumo cero, factores personalizados y manejo de excepciones.

2. **Procesamiento de Métricas y Renderizado Web (Django):**
   - Función `obtener_metricas_consumo(registros)` que procesa el historial de consumo energético por planta industrial, determinando la cantidad de plantas evaluadas, el total global de emisiones ($\text{kg CO}_2$) y la planta con mayor consumo ($\text{kWh}$).
   - Vista `vista_panel_sustentabilidad(request)` y plantilla `sustentabilidad/panel.html` que presentan el resumen ejecutivo y el desglose por planta en una interfaz web limpia.

---

## 📂 Estructura del Proyecto

```text
carpeta_3/
├── ecotech_project/              # Configuración principal del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── sustentabilidad/              # Aplicación de sustentabilidad y emisiones
│   ├── templates/
│   │   └── sustentabilidad/
│   │       └── panel.html        # Plantilla HTML del panel administrativo
│   ├── services.py               # Lógica de cálculo de emisiones y métricas
│   ├── tests.py                  # Suite de pruebas unitarias (unittest)
│   ├── views.py                  # Vistas de Django
│   └── urls.py                   # Rutas de la aplicación
├── manage.py                     # Utilidad CLI de Django
├── requirements.txt              # Dependencias del proyecto
├── .gitignore                    # Archivos excluidos del control de versiones
└── README.md                     # Documentación del proyecto
```

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd carpeta_3
```

### 2. Crear y activar el entorno virtual

En **Windows (PowerShell)**:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

En **Linux / macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecución de Pruebas Unitarias

Puedes ejecutar la auditoría de tests unitarios de cualquiera de las siguientes dos formas:

- **Mediante el runner de pruebas de Django:**
  ```bash
  python manage.py test sustentabilidad -v 2
  ```

- **Ejecutando directamente el archivo de tests con `unittest`:**
  ```bash
  python sustentabilidad/tests.py
  ```

---

## 🖥️ Ejecución del Servidor Web Local

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Luego abre tu navegador en cualquiera de las siguientes direcciones:
- **http://127.0.0.1:8000/sustentabilidad/panel/**
- **http://127.0.0.1:8000/**

---

## 📊 Métricas de Muestra Incluidas

| Planta Industrial | Consumo (kWh) | Emisiones Generadas (kg CO₂) |
| :--- | :---: | :---: |
| **Planta Sucutrule** | 1200.0 kWh | 480.0 kg CO₂ |
| **Planta EaPePé** | 1850.5 kWh | 740.2 kg CO₂ |
| **Planta BlackTuple** | 950.0 kWh | 380.0 kg CO₂ |
| **Planta Pipi Cucú** | 620.0 kWh | 248.0 kg CO₂ |

- **Plantas Evaluadas:** `4`
- **Total Global de Emisiones:** `1848.2 kg CO2`
- **Planta de Mayor Consumo:** `Planta EaPePé (1850.5 kWh)`

---

## ✒️ Autor

Desarrollado por **Sucutrule Productions** `8-)`

