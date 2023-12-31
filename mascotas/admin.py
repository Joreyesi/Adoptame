# mascotas/admin.py

from django.contrib import admin
from .models import Mascota, MascotaAdoptada, Usuario, SuperUsuario, Organizacion, Estado, Publicacion, Galeria, Comuna, Region

admin.site.register(Mascota)
admin.site.register(MascotaAdoptada)
admin.site.register(Usuario)
admin.site.register(SuperUsuario)
admin.site.register(Organizacion)
admin.site.register(Estado)
admin.site.register(Publicacion)
admin.site.register(Galeria)
admin.site.register(Comuna)
admin.site.register(Region)
