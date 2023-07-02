from django.shortcuts import render
from AppRecetas.forms import busca_receta_form#, busca_categoria_form
from .models import Recetas#, Categoría

##revisar

def Inicio(request):
    return render(request, "AppRecetas/index.html")

def AcercaDeMi(request):
     return render(request, "AppRecetas/acerca_de_mi.html")

def BusquedaReceta(request):
     if request.method == "POST":
          busca_receta= busca_receta_form(request.POST)
          if busca_receta.is_valid():
               info = busca_receta.cleaned_data
               receta = Recetas.objects.get(titulo= info["titulo"])
               return render(request, "AppRecetas/recetas_detalle.html", {"receta": receta})
     else: 
          busca_receta = busca_receta_form()
          return render(request, "AppRecetas/recetas_list.html", {"miFormulario": busca_receta})
     '''
def BusquedaCategoria(request):
     if request.method == "POST":
          busca_categoria= busca_categoria_form(request.POST)
          if busca_categoria.is_valid():
               info = busca_categoria.cleaned_data
               categoria = Categoría.objects.filter(nombre= info["nombre"])
               return render(request, "AppRecetas/descripcion_categoria.html", {"categoria": categoria})
     else: 
          busca_categoria = busca_categoria_form()
          return render(request, "AppRecetas/busqueda_categoria.html", {"miFormulario": busca_categoria})
     
'''