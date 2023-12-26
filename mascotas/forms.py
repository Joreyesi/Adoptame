# mascotas/forms.py

from django import forms
from .models import Mascota
from datetime import date
from bootstrap_datepicker_plus import DatePickerInput


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        exclude = ['rut_usuario']
        today = date.today()
        widgets = {
            'fecha_nac_m': DatePickerInput(options={
                'format': 'YYYY-MM-DD',  # El formato que prefieras
                'minDate': '2000-01-01',  # La fecha mínima permitida
                'maxDate': today.strftime('%Y-%m-%d'),  # La fecha máxima permitida
                'showClose': True,
                'showClear': True,
                'showTodayButton': True,
            })
        }

    # Agrega este método para manejar el campo de imagen
    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False  # Permite que la imagen sea opcional
        self.fields['imagen'].widget.attrs['accept'] = 'image/*'  # Acepta cualquier tipo de imagen

    def save(self, commit=True):
        instance = super(MascotaForm, self).save(commit=commit)
        return instance
    