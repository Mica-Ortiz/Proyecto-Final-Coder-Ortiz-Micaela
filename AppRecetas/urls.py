from django.urls import path
from AppRecetas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('recetas/', views.recetas, name="Recetas"),
    path('categorias/', views.categorias, name="Categorías"),
    path('comentarios/', views.comentarios, name="Comentarios"),
    path('formulario_receta/',views.RecetaFormulario, name="Formulario-Receta"),
    path('formulario_categoria/',views.CategoriaFormulario, name="Formulario-Categoría"),
    path('formulario_usuario/',views.UsuarioFormulario, name="Formulario-Usuario"),
    path('busqueda_receta/',views.BusquedaReceta, name="Formulario-Buscar-Receta"),
    path('busqueda_categoria/',views.BusquedaCategoria, name="Formulario-Buscar-Categoria"),
    path('busqueda_usuario/',views.BusquedaUsuario, name="Formulario-Buscar-Usuario")
]