from django.shortcuts import render

def inicio(request):
    return render(request, "AppRecetas/index.html")

def recetas(request):
    return render(request, "AppRecetas/recetas.html")

def categorias(request):
    return render(request, "AppRecetas/categorias.html")

def comentarios(request):
    return render(request, "AppRecetas/comentarios.html")