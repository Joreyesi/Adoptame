# mascotas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('listado_mascotas/', views.listado_mascotas, name='listado_mascotas'),
    path('ingresar_mascota/', views.ingresar_mascota, name='ingresar_mascota'),
    path('eliminar_mascota/<int:mascota_id>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('adoptar_mascota/<int:mascota_id>/', views.adoptar_mascota, name='adoptar_mascota'),  # Nueva ruta para adoptar
]