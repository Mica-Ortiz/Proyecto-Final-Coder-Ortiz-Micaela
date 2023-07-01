from django.shortcuts import render

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordChangeView, LogoutView

from django.views.generic import DeleteView, DetailView

from django.shortcuts import render, redirect

from Accounts import forms

from Accounts import models

from .models import Account

from django.contrib import messages



# Create your views here.

def register(request):  ##comparar con diapos
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
                #return render (request, 'Accounts/iniciar_sesion.html', {'mensaje': 'datos incorrectos'})
        else:
            messages.error(request, 'Error al iniciar sesión')
            ##return render(request, 'Accounts/iniciar_sesion.html', {"mensaje":"Error al iniciar sesión"})
    form= AuthenticationForm()  #lo creo vacio 
    return render (request, 'Accounts/iniciar_sesion.html', {'formulario': form})


##@login_required ## COMPARAR CON EL DEL PROFE
def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _= models.Account.objects.get_or_create(user=usuario) ##VER BIEN
    if request.method == 'POST':
        form = forms.EditarUsuarioForm(request.POST,request.FILES) ##request.files permite traer las imágenes
        if form.is_valid():
            data = form.cleaned_data
            if data.get('email'):
                usuario.email = data.get('email')
            if data.get('password1'):
                usuario.password1 = data.get('password1')
            if data.get('password2'):
                usuario.password1 = data.get('password2')
            if data.get('last_name'):
                usuario.last_name= data.get('last_name')
            if data.get('first_name'):
                usuario.first_name= data.get('first_name')
            modelo_perfil.avatar = data.get('avatar') if data.get('avatar') else modelo_perfil.avatar ##para cambiar el avatar, la variable no forma parte de user por eso llamo a Account

            usuario.save()
            modelo_perfil.save()

            return redirect ('Inicio') ##cambiar a mostrar account
        else:
            return render(request, "Accounts/editar_account.html", {"formulario": form , "usuario": usuario})
#form = forms.EditarUsuarioForm(initial={'email': usuario.email}) asi estaba en el ppt
## Al entrar con el metodo get se crea una instancia del formulario donde se muestran los valores iniciales/existentes que se indican abajo
    form = forms.EditarUsuarioForm(
        initial= {
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'avatar': modelo_perfil.avatar
        }
    )
    return render(request, "Accounts/editar_account.html", {"formulario": form , "usuario": usuario})



class MostrarPerfilDetailView (DetailView):
    model = Account
    template_name = "Accounts/mostrar_account.html"
    
##en el html request se utiliza para acceder a la información del usuario autenticado.

def eliminar_perfil(request):
    pass

def cambiar_password(request):
    pass

class Logout(LogoutView):
    template_name = 'Accounts/logout_account.html'