from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}  # Eliminar textos de ayuda

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return password2
        
#          ----------------------------------------Form de editar Usuario--------------------------------------------             \
    
class UserEditForm(UserChangeForm):

        # Obligatorios
        password = None
        email = forms.EmailField(label="Ingrese su email:")
        last_name = forms.CharField(label="Apellido")
        first_name = forms.CharField(label="Nombre")
        imagen = forms.ImageField(label="Avatar",required=False)
        
        
        # No obligatorios
        # last_name = forms.CharField()
        # first_name = forms.CharField()

        class Meta:
            model = User
            fields = [
                'email',
                'last_name',
                'first_name',
                'imagen'
                # 'last_name',
                # 'first_name'
            ]
            help_texts = {k:"" for k in fields}

#           ---------------------------------------formulario de Carga de Avatar------------------------------------------------------

