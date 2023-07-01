from django.db import models
import datetime

class Categoría(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Recetas(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=100, null= True, default="")
    ingredientes = models.CharField(max_length=1000)
    pasos = models.CharField(max_length=1000)
    tiempo_de_coccion = models.IntegerField()
    fecha_hora_de_subida = models.DateTimeField(default=datetime.datetime.now)
    categoria = models.ManyToManyField(Categoría)
    imagen = models.ImageField(upload_to ='imagenes', null=True, blank=True)

    def __str__(self):
        return self.titulo






    