from django.db import models

# Create your models here.
class Reseña(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    image = models.ImageField(default='null')
    publicado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=110)
    descripcion = models.CharField(max_length=250)
    creado = models.DateField()

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    fecha_nacimiento = models.DateTimeField(auto_now_add=False)
    pais = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
