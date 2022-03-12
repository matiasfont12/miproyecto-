from django.http import HttpResponse 
import random
from django.template import Template 
from django.template import Context



def inicio(request):
    return HttpResponse("Hola, soy la nueva pagina")

def otra_vista(request):
    return HttpResponse("""""""""""""""
                        <h1>Este mensaje es un titulo en h1<h1>
                         """ )
        
def numero_random(request):
    numero = random.randrange(15,180)
    return HttpResponse        

def mi_plantilla(request):
    plantilla = open(r"C:\Users\Matias\Downloads\Desktop\miproyecto\miproyecto\plantillas\plantillas.html")     
    
    template = Template(plantilla.read())
    
    nombre = "Matias Emanuel"
    apellido = "Font"
    
    diccionario_de_datos = {
      "Nombre": nombre,
      "Apellido": apellido,
    }
    
    context = Context(diccionario_de_datos)
    
    plantilla_lista = template.render(context)
    
    return HttpResponse(plantilla_lista)

 
