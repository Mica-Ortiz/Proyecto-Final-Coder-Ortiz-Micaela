from django.shortcuts import render
from AppRecetas.forms import receta_formulario, categoria_formulario, usuario_formulario, busca_receta_form, busca_categoria_form, busca_usuario_form  
from .models import Recetas, Categoría

##revisar

def inicio(request):
    return render(request, "AppRecetas/index.html")

def recetas(request):
    return render(request, "AppRecetas/recetas-list.html")

def categorias(request):
    return render(request, "AppRecetas/categorias.html")

def comentarios(request):
    return render(request, "AppRecetas/comentarios.html")




def RecetaFormulario(request):
      
      if request.method == "POST":
            miFormulario = receta_formulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  curso = Recetas(titulo=info["titulo"], ingredientes=info["ingredientes"], pasos=info["pasos"], tiempo_de_coccion=info["tiempo_de_coccion"]) 
                  curso.save()
                  return render(request, "AppRecetas/index.html")
      else:
            miFormulario = receta_formulario()
      return render(request, "AppRecetas/formulario_receta.html", {"miFormulario": miFormulario}) 

def CategoriaFormulario(request):
      
      if request.method == "POST":
            miFormulario = categoria_formulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  curso = Categoría(nombre=info["nombre"]) 
                  curso.save()
                  return render(request, "AppRecetas/index.html")
      else:
            miFormulario = categoria_formulario()
      return render(request, "AppRecetas/formulario_categoria.html", {"miFormulario": miFormulario}) 

def UsuarioFormulario(request):
      
      if request.method == "POST":
            miFormulario = usuario_formulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  curso = Usuario(usuario=info["usuario"], contraseña=info["contraseña"], email=info["email"]) 
                  curso.save()
                  return render(request, "AppRecetas/index.html")
      else:
            miFormulario = usuario_formulario()
      return render(request, "AppRecetas/formulario_usuario.html", {"miFormulario": miFormulario}) 




def BusquedaReceta(request):
     if request.method == "POST":
          busca_receta= busca_receta_form(request.POST)
          if busca_receta.is_valid():
               info = busca_receta.cleaned_data
               receta = Recetas.objects.filter(titulo= info["titulo"])
               return render(request, "AppRecetas/descripcion_recetas.html", {"recetas": receta})
     else: 
          busca_receta = busca_receta_form()
          return render(request, "AppRecetas/busqueda_receta.html", {"miFormulario": busca_receta})
     
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
     
def BusquedaUsuario(request):
     if request.method == "POST":
          busca_usuario= busca_usuario_form(request.POST)
          if busca_usuario.is_valid():
               info = busca_usuario.cleaned_data
               usuario = Usuario.objects.filter(usuario= info["usuario"])
               return render(request, "AppRecetas/descripcion_usuario.html", {"usuario": usuario})
     else: 
          busca_usuario = busca_usuario_form()
          return render(request, "AppRecetas/busqueda_usuario.html", {"miFormulario": busca_usuario})