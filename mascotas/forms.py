# mascotas/forms.py

from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'  # Puedes personalizar esto según las necesidades

# Otros formularios pueden ir aquí si es necesario
