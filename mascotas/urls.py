# mascotas/urls.py

from django.urls import path
from .views import listado_mascotas, ingresar_mascota

urlpatterns = [
    path('listado_mascotas/', listado_mascotas, name='listado_mascotas'),
    path('ingresar_mascota/', ingresar_mascota, name='ingresar_mascota'),
    # Otras rutas pueden ir aquí
]