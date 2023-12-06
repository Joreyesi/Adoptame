from django.shortcuts import render

# Create your views here.
# En tu archivo views.py

from .models import Mascota

def listado_animales(request):
    animales = Mascota.objects.all()
    return render(request, 'listado_animales.html', {'animales': animales})
