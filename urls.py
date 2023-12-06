# tu_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', include('mascotas.urls')),  # Asegúrate de incluir correctamente las rutas de tu aplicación
    # Otras rutas pueden ir aquí
]