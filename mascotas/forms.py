from django import forms
from .models import Mascota, Usuario, SuperUsuario
from datetime import date
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import DateInput


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        exclude = ['rut_usuario']
        widgets = {
            'fecha_nac_m': forms.TextInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)

        # Obtener las opciones de animal desde el modelo
        animal_choices = Mascota.ANIMAL_CHOICES

        # Obtener el tipo de animal actual (si está presente)
        animal_value = self.initial.get('animal_m') or (self.instance.animal_m if self.instance.pk else None)

        # Obtener las opciones de raza correspondientes al tipo de animal
        raza_options = Mascota.RAZA_CHOICES.get(animal_value, [])

        # Agregar la opción por defecto si no está presente y animal_value no es None
        if animal_value is not None and ('', '---------') not in raza_options:
            raza_options.insert(0, ('', '---------'))

        # Utilizar el widget directamente para establecer las opciones
        self.fields['raza_m'].widget = forms.Select(choices=raza_options)






    

class DateInput(forms.DateInput):
    input_type = 'date'

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('rut_usuario','nombre_u', 'apellido_u', 'genero_u', 'fecha_nac_u', 'id_u', 'password1', 'password2','email','telefono_u', 'ciudad_u')
        labels = {
        'rut_usuario': 'Rut usuario',
        'nombre_u': 'Nombre',
        'apellido_u': 'Apellido',
        'genero_u': 'Género',
        'fecha_nac_u': 'Fecha de nacimiento',
        'id_u': 'ID Usuario',
        'password1': 'Contraseña',
        'password2': 'Confirmación de contraseña',
        'email': 'Email',
        'telefono_u': 'Teléfono',
        'ciudad_u': 'Ciudad',
    }
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