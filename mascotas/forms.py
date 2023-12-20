# mascotas/forms.py

from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'fecha_nac_m': forms.DateInput(attrs={'type': 'date'}),
            # Puedes agregar más personalizaciones aquí según tus necesidades
        }

# Otros formularios pueden ir aquí si es necesario
