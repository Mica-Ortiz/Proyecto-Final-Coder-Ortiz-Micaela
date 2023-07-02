from django.urls import path
from Accounts import views



urlpatterns = [
    path('register/', views.register, name= 'Register'),
    path('login/', views.login_request, name= 'Login'),
    path('logout/', views.Logout.as_view(), name= 'Logout'),
    path('editarPerfil/', views.editar_perfil, name= 'EditarPefil'),
    path('mostrarPerfil/', views.mostrar_perfil, name='MostrarPerfil'),
    path('eliminarPerfil/<pk>/', views.EliminarPerfil.as_view(), name='EliminarPerfil'),
    path('busquedaUsuario/',views.buscar_usuario, name="Formulario-Buscar-Usuario"),
]
