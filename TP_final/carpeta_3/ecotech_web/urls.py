from django.urls import path
from sustentabilidad.views import vista_panel_sustentabilidad

# Cuando se ingresa a la página principal ("") se ejecuta vista_panel_sustentabilidad
urlpatterns = [
    path("", vista_panel_sustentabilidad),
]
