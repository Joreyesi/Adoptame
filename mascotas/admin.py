# mascotas/admin.py

from django.contrib import admin
from .models import Mascota, Usuario, Organizacion, Estado, Publicacion, Galeria, Comuna, Region

admin.site.register(Mascota)
admin.site.register(Usuario)
admin.site.register(Organizacion)
admin.site.register(Estado)
admin.site.register(Publicacion)
admin.site.register(Galeria)
admin.site.register(Comuna)
admin.site.register(Region)
