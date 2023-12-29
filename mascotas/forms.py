from django import forms
from .models import Mascota, Usuario, SuperUsuario
from datetime import date
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
    

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class SuperUsuarioForm(forms.ModelForm):
    class Meta:
        model = SuperUsuario
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('nombre_u', 'apellido_u', 'genero_u', 'fecha_nac_u', 'id_u', 'contraseña_u', 'telefono_u', 'ciudad_u', 'tipo_usuario_u')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Eliminar campos relacionados con el superusuario
        del self.fields['is_staff']
        del self.fields['is_superuser']
        del self.fields['groups']
        del self.fields['user_permissions']
        del self.fields['last_login']
        del self.fields['date_joined']

