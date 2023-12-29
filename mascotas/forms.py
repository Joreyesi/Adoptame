from django import forms
from .models import Mascota, Usuario, SuperUsuario
from datetime import date
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import DateInput


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        exclude = ['rut_usuario']
        today = date.today()
        widgets = {
            'fecha_nac_m': forms.TextInput(attrs={'type': 'date'}),
        }

    # Agrega este método para manejar el campo de imagen
    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False  # Permite que la imagen sea opcional
        self.fields['imagen'].widget.attrs['accept'] = 'image/*'  # Acepta cualquier tipo de imagen

    def save(self, commit=True):
        instance = super(MascotaForm, self).save(commit=commit)
        return instance
    

class DateInput(forms.DateInput):
    input_type = 'date'

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('rut_usuario','nombre_u', 'apellido_u', 'genero_u', 'fecha_nac_u', 'id_u', 'password1', 'password2','telefono_u', 'ciudad_u')
        widgets = {
            'fecha_nac_u': DateInput(),
        }

class SuperUsuarioForm(forms.ModelForm):
    class Meta:
        model = SuperUsuario
        fields = '__all__'

class CustomUserCreationForm(UsuarioCreationForm):
    class Meta(UsuarioCreationForm.Meta):
        fields = UsuarioCreationForm.Meta.fields
        exclude = ('is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined', 'id_u')  # Excluir id_u si ya está en UsuarioCreationForm


