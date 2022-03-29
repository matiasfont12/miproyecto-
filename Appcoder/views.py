from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import Curso
import random


def nuevo_curso(request):
    curso = random.randrange(1500,3000)
    nuevo_curso = Curso(nombre = "Curso Python", curso=curso)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} {nuevo_curso.curso}")

def formulario_curso(request):
  
    print(request.method)
  
    if request.method == "POST":
      print(request.POST)
    
      nuevo_curso = Curso(nombre=request.POST["nombre"], curso=request.POST["curso"])
      nuevo_curso.save()
     
      return render(request, "Appcoder/formulario.html", {"nuevo_curso":nuevo_curso}) 
      
    return render(request, "Appcoder/formulario.html", {})

      
   
    