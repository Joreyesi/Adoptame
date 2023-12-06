# En tu archivo urls.py (de la aplicación)
from django.urls import path
from .views import listado_animales

urlpatterns = [
    path('Template/listado_animales/', listado_animales, name='listado_animales'),
    # Otras URL de tu aplicación...
]