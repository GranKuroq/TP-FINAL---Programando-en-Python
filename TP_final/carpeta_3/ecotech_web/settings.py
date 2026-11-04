import os

# Ruta de la carpeta principal del proyecto (carpeta_3)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Clave de prueba para desarrollo local
SECRET_KEY = "clave-secreta-ecotech-solutions"

# Modo de prueba activado para ver detalles en caso de error
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Aplicaciones instaladas en nuestro proyecto
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "sustentabilidad",
]

MIDDLEWARE = []

# Archivo donde están definidas las rutas web principales
ROOT_URLCONF = "ecotech_web.urls"

# Configuración para que Django busque los archivos HTML dentro de cada app (carpeta templates)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
    },
]

WSGI_APPLICATION = "ecotech_web.wsgi.application"

# Base de datos local por defecto (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
STATIC_URL = "static/"
