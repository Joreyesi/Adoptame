# En tu archivo urls.py (del proyecto)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', include('mascotas.urls')),  # Reemplaza 'tuapp' con el nombre real de tu aplicación
]