from django import forms
from .models import Mascota, Usuario, SuperUsuario
from datetime import date
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import DateInput


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        exclude = ['rut_usuario']  # Puedes excluir campos adicionales si es necesario
        widgets = {
            'fecha_nac_m': forms.TextInput(attrs={'type': 'date'}),
        }

    # Agrega este método para manejar el campo de imagen
    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False
        self.fields['imagen2'].required = False
        self.fields['imagen'].widget.attrs['accept'] = 'image/*'
        self.fields['imagen2'].widget.attrs['accept'] = 'image/*'

    def save(self, commit=True):
        instance = super(MascotaForm, self).save(commit=commit)
        return instance
    

class DateInput(forms.DateInput):
    input_type = 'date'

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('rut_usuario','nombre_u', 'apellido_u', 'genero_u', 'fecha_nac_u', 'id_u', 'password1', 'password2','email','telefono_u', 'ciudad_u')
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
        exclude = ('is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined')  # Excluir id_u si ya está en UsuarioCreationForm



class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        # Este método evita la verificación de 'is_staff'
        pass


class CustomFileInput(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        template_name = 'custom_file_input.html'  # Puedes crear un archivo HTML personalizado
        context = {'widget': self, 'name': name, 'value': value, 'attrs': attrs}
        return super().render(name, value, attrs, renderer)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # Añade atributos para especificar el tamaño máximo
        context['widget']['attrs'].update({'accept': 'image/*', 'onchange': 'resizeImage(this)'})
        return context