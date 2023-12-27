# En tu archivo urls.py del proyecto
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', include('mascotas.urls')),
]

# Configuración para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


