# mascotas/urls.py

from django.urls import path
from .views import listado_animales  # Asegúrate de importar la vista correcta

urlpatterns = [
    path('listado_animales/', listado_animales, name='listado_animales'),
    # Otras rutas pueden ir aquí
]