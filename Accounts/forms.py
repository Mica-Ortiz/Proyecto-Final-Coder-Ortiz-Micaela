from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class RegistroUsuarioForm (UserCreationForm):
    email = forms.EmailField (label= "Email")
    password1 = forms.CharField (label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField (label= "Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditarUsuarioForm (forms.Form):
    email = forms.EmailField(required=False)

    #lo siguiente no cambia la contraseña. habria que poner algo para que te pida la contraseña para editar el perfil, aunque este logueado.
    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre", max_length=30, required=False)
    last_name = forms.CharField(label="Apellido", max_length=30, required=False)
    avatar = forms.ImageField(required=False)

class busca_usuario_form(forms.Form):
    usuario = forms.CharField()