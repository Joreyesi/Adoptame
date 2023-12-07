# mascotas/urls.py

from django.urls import path
from .views import listado_animales

urlpatterns = [
    path('mascotas/listado_animales/', listado_animales, name='listado_animales'),
    # Otras rutas pueden ir aquí
]