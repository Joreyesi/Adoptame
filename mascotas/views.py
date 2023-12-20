from django.shortcuts import render

# Create your views here.
# En tu archivo views.py

from .models import Mascota

def listado_animales(request):
    animales = Mascota.objects.all()
    return render(request, 'mascotas/listado_animales.html')


def ingresar_mascota(request):
    # Lógica para ingresar mascota (puede ser un formulario)
    return render(request, 'mascotas/ingresar_mascota.html')