from django.shortcuts import redirect, render
from .models import Persona
from .forms import PersonaForm

# vistas basadas en funciones sin usar clases


def inicio(request):
    personas = Persona.objects.all()  # SELECT * FROM Persona ORM Django
    contexto = {  # diccionario para enviar personas
        'personas': personas
    }
    return render(request, 'index.html', contexto)


def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form': form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()  #si los campos son validos, que los cargue en la base de datos.
            return redirect('index') #luego de eso que me redireccione al index.html, lo hago especificando el nombre de la ruta.
        print(form)

    return render(request, 'crear_persona.html', contexto)

def editarPersona(request,id): #recibe el id para buscar el registro a editar en la bd
    persona = Persona.objects.get(id = id)  #obtener el registro cuyo id sea igual al id recibido por parámetro.
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST, instance = persona) #En caso de ser la modificación de un registro existente.
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_persona.html',contexto)

def eliminarPersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')

