# mascotas/forms.py

from django import forms
from django.forms import SelectDateWidget
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        exclude = ['rut_usuario']
        widgets = {
            'fecha_nac_m': SelectDateWidget(years=range(2000, 'today'))
        }

    # Agrega este método para manejar el campo de imagen
    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False  # Permite que la imagen sea opcional
        self.fields['imagen'].widget.attrs['accept'] = 'image/*'  # Acepta cualquier tipo de imagen

    def save(self, commit=True):
        instance = super(MascotaForm, self).save(commit=commit)
        return instance
    