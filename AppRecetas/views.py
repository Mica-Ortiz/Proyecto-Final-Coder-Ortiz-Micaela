from django.shortcuts import render, redirect, get_object_or_404
from AppRecetas.forms import busca_receta_form, busca_categoria_form
from .models import Recetas, Categoría
from django.contrib import messages



def Inicio(request):
    categorias = Categoría.objects.all()
    recetas = Recetas.objects.all()
    return render(request, "AppRecetas/index.html", {'categorias': categorias, "recetas": recetas})
    

def AcercaDeMi(request):
     return render(request, "AppRecetas/acerca_de_mi.html")

def BusquedaReceta(request):
     if request.method == "POST":
          busca_receta= busca_receta_form(request.POST)
          if busca_receta.is_valid():
               info = busca_receta.cleaned_data
               receta = Recetas.objects.filter(titulo__icontains= info["titulo"])
               if receta.exists():
                    return render(request, "AppRecetas/recetas_detalle_buscar.html", {"receta": receta})
               else:
                    messages.error(request, 'No se encontraron resultados')
                    return redirect ('Formulario-Buscar-Receta')
     else: 
          busca_receta = busca_receta_form()
          return render(request, "AppRecetas/busqueda_receta.html", {"miFormulario": busca_receta})
     
def BusquedaCategoria(request):
     if request.method == "POST":
          busca_categoria= busca_categoria_form(request.POST)
          if busca_categoria.is_valid():
               info = busca_categoria.cleaned_data
               try:
                    categoria = Categoría.objects.get(nombre= info["nombre"])
                    recetas = categoria.recetas.all()
                    return render(request, "AppRecetas/listado_categoria.html", {"categoria": categoria, "recetas":recetas})
               except Categoría.DoesNotExist:
                    messages.error(request, 'No se encontraron resultados')
                    return redirect ('Formulario-Buscar-Categoria')
     else: 
          busca_categoria = busca_categoria_form()
          return render(request, "AppRecetas/busqueda_categoria.html", {"miFormulario": busca_categoria})

def RecetasPorCategoria(request, categoria_id):
    categoria = get_object_or_404(Categoría, id=categoria_id)
    recetas = Recetas.objects.filter(categoria=categoria)
    return render(request, "AppRecetas/listado_categoria.html", {"categoria": categoria, "recetas":recetas})