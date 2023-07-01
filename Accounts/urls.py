from django.urls import path
from Accounts import views
from .views import MostrarPerfilDetailView , Logout 


urlpatterns = [
    path('register/', views.register, name= 'Register'),
    path('login/', views.login_request, name= 'Login'),
    path('logout/', views.Logout.as_view(), name= 'Logout'),
    path('editarPerfil/', views.editar_perfil, name= 'EditarPefil'),
    path('mostrarPerfil', views.MostrarPerfilDetailView.as_view(), name= 'MostrarPerfil'),
]
