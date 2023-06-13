from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.usuario
    
    def save(self, *args, **kwargs):
        self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

class Recetas(models.Model):
    titulo = models.CharField(max_length=40)
    ingredientes = models.CharField(max_length=100)
    pasos = models.CharField(max_length=100)
    tiempo_de_coccion = models.IntegerField()


class Categoría(models.Model):
    nombre = models.CharField(max_length=20)

class Comentarios(models.Model):
    contenido = models.CharField(max_length=200)
    comentador = Usuario.usuario
    fecha = models.DateField()


    