# mascotas/urls.py
from django.urls import path, include
from . import views
from .views import (
    registrar_usuario, 
    registrar_superusuario, 
    home, 
    user_home,
    logeado,
    LoginView  # Importa la vista de inicio de sesión
)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LogoutView
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm

app_name = 'mascotas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listado_mascotas/', views.listado_mascotas, name='listado_mascotas'),
    path('ingresar_mascota/', views.ingresar_mascota, name='ingresar_mascota'),
    path('eliminar_mascota/<int:mascota_id>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('adoptar_mascota/<int:mascota_id>/', views.adoptar_mascota, name='adoptar_mascota'),
    path('adoptar_mascota_lista/', views.adoptar_mascota_lista, name='adoptar_mascota_lista'),
    path('user_login/', registrar_usuario, name='user_login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Agrega la URL para la vista de inicio de sesión
    path('logout/', LogoutView.as_view(next_page='/home/'), name='logout'),
    path('admin_login/', registrar_superusuario, name='admin_login'),
    path('home/', home, name='home'),
    path('user/home/', user_home, name='user_home'),
    path('registrar-usuario/', registrar_usuario, name='registrar_usuario'),
    path('registrar-superusuario/', registrar_superusuario, name='registrar_superusuario'),
    path('logeado/', logeado, name='logeado'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
