from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import Curso
from Appcoder.forms import CursoFormulario, BusquedaNombre
import random


def nuevo_curso(request):
    curso = random.randrange(1500,3000)
    nuevo_curso = Curso(nombre = "Curso Python", curso=curso)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} {nuevo_curso.curso}")

def formulario_curso(request):
  
  formulario = CursoFormulario()
  
  if request.method == "POST":
    formulario = CursoFormulario(request.POST)
    print(request.POST)
  if formulario.is_valid():
    data = formulario.cleaned_data
    nuevo_curso = Curso(nombre=data["nombre"], curso=data["curso"])
    nuevo_curso.save()
    
    return render(request,"Appcoder/formulario.html",{"nuevo_curso":nuevo_curso})
    
    
  
  else:
   formulario = CursoFormulario()
   return render(request,"Appcoder/formulario.html",{"formulario":formulario})
  
def busqueda_nombre(request):
  
  nombre_buscado = []
  
  dato = request.GET.get("nombre", None)
  if dato is not None:
    nombre_buscado = Curso.objects.filter(nombre__icontains=dato)

  busqueda = BusquedaNombre()
  

  return render(request,"Appcoder/busqueda_nombre.html",
                {"busqueda": busqueda, 
                 "nombre_buscado": nombre_buscado,
                 "dato": dato})