# tu_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mascotas.urls')),  # Use una ruta vacía para la aplicación principal
    # Otras rutas pueden ir aquí
]
