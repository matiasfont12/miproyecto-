from django.urls import path
from .views import nuevo_curso, formulario_curso, busqueda_nombre

urlpatterns = [
    path("nuevo/",nuevo_curso, name= "nuevo_curso"),
    path("curso/", formulario_curso, name= "formulario"),
    path("busqueda_nombre/", busqueda_nombre, name= "busqueda_nombre")
  
]
