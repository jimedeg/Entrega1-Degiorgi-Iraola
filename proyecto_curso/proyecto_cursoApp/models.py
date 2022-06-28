from distutils.log import info
from django.db import models
from django.forms import Textarea

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    info = models.CharField(max_length=100)
    fecha = models.DateTimeField()
        
class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    info = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    
    
class Comentrio(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField(Textarea)  