from django.urls import path
from AppRecetas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('recetas/', views.recetas, name="Recetas"),
    path('categorias/', views.categorias, name="Categorías"),
    path('comentarios/', views.comentarios, name="Comentarios")
]