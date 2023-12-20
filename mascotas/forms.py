# mascotas/forms.py

from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        exclude = ['rut_usuario']
        widgets = {
            'fecha_nac_m': forms.TextInput(attrs={'type': 'date'}),
            # Puedes agregar más personalizaciones aquí según tus necesidades
        }

