# mascotas/urls.py

from django.urls import path
from .views import listado_animales
from .views import ingresar_mascota

urlpatterns = [
    path('templates/listado_animales/', listado_animales, name='listado_animales'),
    # Otras rutas pueden ir aquí
]


urlpatterns = [
    path('ingresar_mascota/', ingresar_mascota, name='ingresar_mascota'),
    # Otras rutas pueden ir aquí
]