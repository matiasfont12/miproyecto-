from django.http import HttpResponse 
import random
from django.template import Template, Context, loader




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
    #plantilla = open(r"C:\Users\Matias\Downloads\Desktop\miproyecto\miproyecto\plantillas\plantillas.html")     
    #template = Template(plantilla.read())
    
    nombre = "matias emanuel"
    apellido = "font"
    lista = [1,2,3,4,5]
    
    diccionario_de_datos = {
     "nombre": nombre,
     "apellido": apellido,
     "lista": lista
    }
    
    template = loader.get_template("plantillas.html")
    
    plantilla_lista = template.render(diccionario_de_datos)
    
    #context = Context(diccionario_de_datos)
    
    return HttpResponse(plantilla_lista)
 
