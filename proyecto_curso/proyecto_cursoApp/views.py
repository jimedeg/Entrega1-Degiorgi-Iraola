from django.shortcuts import render,redirect
from django.http import HttpResponse

from proyecto_cursoApp.models import Curso, Evento
from .forms import nuevo_curso, nuevo_evento
from django.db.models import Q

# Create your views here.
def inicio (request):
    
    curso = Curso.objects.all()[:3]
    evento = Evento.objects.all()[:3]
    
    return render(request,"proyecto_cursoApp/index.html",{'curso': curso , 'evento': evento})


def curso (request):
    
    if request.method == "POST":

        buscar = request.POST["buscar"]

        if buscar != "":
            curso = Curso.objects.filter( Q(nombre__icontains=buscar)).values()

            return render(request,"proyecto_cursoApp/curso.html",{"curso":curso, "buscar":True, "busqueda":buscar})

    curso = Curso.objects.all()

    return render(request,"proyecto_cursoApp/curso.html",{"curso":curso, "buscar":False})
  
   

def evento (request):
    if request.method == "POST":

        buscar = request.POST["buscar"]

        if buscar != "":
            evento = Evento.objects.filter( Q(nombre__icontains=buscar)).values()

            return render(request,"proyecto_cursoApp/evento.html",{"evento":evento, "buscar":True, "busqueda":buscar})

    evento = Evento.objects.all()

    return render(request,"proyecto_cursoApp/evento.html",{"evento":evento, "buscar":False})

def contacto (request):
    
    return render(request,"proyecto_cursoApp/contacto.html",{})

def crear_curso (request):
    #post
    if request.method == "POST":
        
        formulario = nuevo_curso(request.POST)
        
        if formulario.is_valid():
            
            info_curso = formulario.cleaned_data
            
            curso = Curso(nombre = info_curso ["nombre"], info = info_curso ["informacion"], fecha = info_curso ["fecha"] )
            curso.save() #Guardar en la db
            
            return redirect("curso")
        else:
            return render(request,"proyecto_cursoApp/crear_curso.html",{"form":formulario})
    else:
        
        formulario_vacio= nuevo_curso()
         
        return render(request,"proyecto_cursoApp/crear_curso.html",{"form":formulario_vacio})

def crear_evento (request):
    #post
    if request.method == "POST":
        
        form = nuevo_evento(request.POST)
        
        if form.is_valid():
            
            info_evento = form.cleaned_data
            
            evento = Evento(nombre = info_evento ["nombre"], info = info_evento ["info"], fecha = info_evento ["fecha"] )
            evento.save() #Guardar en la db
            
            return redirect("evento")
        else:
            return render(request,"proyecto_cursoApp/crear_evento.html",{"form":form})
    else:
        
        form_vacio= nuevo_evento()
         
        return render(request,"proyecto_cursoApp/crear_evento.html",{"form":form_vacio})
               
def busqueda (request):
         
    if request.method == "POST":
        
        nombre = request.POST["nombre"] 
             
        busquedas = Curso.objects.filter(nombre__icontains=nombre)
        
        return render(request,"proyecto_cursoApp/busqueda.html",{"busquedas": busquedas})
  
    else:
        
        busquedas=[]
        
        return render(request,"proyecto_cursoApp/busqueda.html",{"busquedas": busquedas})
       