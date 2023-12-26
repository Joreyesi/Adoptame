# mascotas/forms.py

from django import forms
from django.forms import SelectDateWidget
from .models import Mascota
from datetime import date
import calendar


class CustomSelectDateWidget(SelectDateWidget):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        # Obtener los valores actuales para año, mes y día
        year = context['widget']['year']
        month = context['widget']['month']
        day = context['widget']['day']

        # Obtener el número máximo de días para el mes y año actual
        max_days = calendar.monthrange(year, month)[1]

        # Ajustar la cantidad de días en el widget
        context['widget']['days'] = [
            (i, '%02d' % i) for i in range(1, max_days + 1)
        ]

        return context

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        exclude = ['rut_usuario']
        today = date.today()
        widgets = {
            'fecha_nac_m': CustomSelectDateWidget(years=range(2000, today.year + 1))
        }

    # Agrega este método para manejar el campo de imagen
    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False  # Permite que la imagen sea opcional
        self.fields['imagen'].widget.attrs['accept'] = 'image/*'  # Acepta cualquier tipo de imagen

    def save(self, commit=True):
        instance = super(MascotaForm, self).save(commit=commit)
        return instance
    