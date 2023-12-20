from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm 


# Create your views here.
# En tu archivo views.py


def listado_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listado_mascotas.html', {'mascotas': mascotas})


def ingresar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_mascotas')
    else:
        form = MascotaForm()

    return render(request, 'mascotas/ingresar_mascota.html', {'form': form})