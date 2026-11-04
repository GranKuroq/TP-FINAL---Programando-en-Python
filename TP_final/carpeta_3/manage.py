import os
import sys
from django.core.management import execute_from_command_line

# Archivo principal de Django para ejecutar el servidor local con: python manage.py runserver
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecotech_web.settings")
    execute_from_command_line(sys.argv)
