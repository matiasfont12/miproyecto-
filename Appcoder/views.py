from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import Curso
import random


def nuevo_curso(request):
    curso = random.randrange(1500,3000)
    nuevo_curso = Curso(nombre = "Curso Python", curso=curso)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} {nuevo_curso.curso}")
