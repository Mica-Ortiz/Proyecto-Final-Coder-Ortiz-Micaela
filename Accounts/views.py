from django.shortcuts import render

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import PasswordChangeView, LogoutView

from django.views.generic import DeleteView

from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from Accounts import forms

from Accounts import models

from .models import Account

from django.contrib import messages


# Create your views here.

def register(request):  
    if request.method == 'POST':
        form= forms.RegistroUsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
        else:
            return render (request, 'Accounts/crear_account.html', {'formulario': form})
    form= forms.RegistroUsuarioForm()  #lo creo vacio 
    return render (request, 'Accounts/crear_account.html', {'formulario': form})


def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password =contraseña)
            if user is not None:
                login(request, user)
                return redirect ('Inicio') ##cuando inicia sesion va a la pagina inicial
            else:
                messages.error(request, 'Datos incorrectos')
        else:
            messages.error(request, 'Error al iniciar sesión')
    form= AuthenticationForm()  #lo creo vacio 
    return render (request, 'Accounts/iniciar_sesion.html', {'formulario': form})


@login_required
def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _= models.Account.objects.get_or_create(user=usuario) ##VER BIEN
    if request.method == 'POST':
        form = forms.EditarUsuarioForm(request.POST,request.FILES) ##request.files permite traer las imágenes
        if form.is_valid():
            data = form.cleaned_data
            
            usuario.email = data['email']
            usuario.last_name = data['last_name']
            usuario.first_name = data['first_name']

            modelo_perfil.avatar = data.get('avatar') if data.get('avatar') else modelo_perfil.avatar ##para cambiar el avatar, la variable no forma parte de user por eso llamo a Account

            usuario.save()
            modelo_perfil.save()

            return render(request, "Accounts/mostrar_account.html", {"formulario": form , "usuario": usuario, "perfil":modelo_perfil})
        else:
            return render(request, "Accounts/editar_account.html", {"formulario": form , "usuario": usuario})
    form = forms.EditarUsuarioForm(
        initial= {
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'avatar': modelo_perfil.avatar
        }
    )
    return render(request, "Accounts/editar_account.html", {"formulario": form , "usuario": usuario})

def mostrar_perfil(request):
    usuario = request.user
    perfil,_ = Account.objects.get_or_create(user=usuario)
    return render(request, "Accounts/mostrar_account.html", {"user": usuario, "perfil":perfil})

class EliminarPerfil(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("Inicio")
    template_name = 'Accounts/eliminar_account.html'

def cambiar_password(request):
    pass

class Logout(LogoutView):
    template_name = 'Accounts/logout_account.html'

def buscar_usuario(request):
    if request.method == "POST":
        busca_usuario= forms.busca_usuario_form(request.POST)
        if busca_usuario.is_valid():
            info = busca_usuario.cleaned_data
            try:
                usuario = User.objects.get(username= info["usuario"])
                perfil,_ = Account.objects.get_or_create(user=usuario)
                return render(request, "Accounts/mostrar_account.html", {"user": usuario, "perfil":perfil})
            except User.DoesNotExist:
                messages.error(request, 'No se encontró el usuario')
                return redirect ('Formulario-Buscar-Usuario')
        else:
            messages.error(request, 'No se encontraron resultados')
            return redirect ('Formulario-Buscar-Usuario')
    else: 
        busca_usuario= forms.busca_usuario_form()
        return render(request, "Accounts/busqueda_usuario.html", {"miFormulario": busca_usuario})