from turtle import textinput
from django import forms

class nuevo_curso(forms.Form):
    
    nombre = forms.CharField(max_length= 30)
    informacion = forms.CharField(max_length=100)
    fecha = forms.DateTimeField()
    
class nuevo_evento(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    info = forms.CharField(max_length=100)
    fecha = forms.DateTimeField()
    
class nuevo_comentario(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField()