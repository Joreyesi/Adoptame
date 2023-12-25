# tu_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mascotas.urls')),  # Use una ruta vacía para la aplicación principal
    # Otras rutas pueden ir aquí
]

# Agrega estas líneas al final para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)