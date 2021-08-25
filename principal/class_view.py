from principal.views import crearPersona
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .forms import PersonaForm
from .models import Persona
from django.urls import reverse_lazy

'''
dispath: verifica el método de solicitud http
http_not_allowed

class ListView():
    model = Persona
    template_name = 'index.html'  (Estas 2 líneas contienen las siguientes 3 funciones)

    def gett(self,request,*args,**kwargs): 
        return render(request,self.get_templates_names(),self.get_queryset())

    def get_queryset(self):
        return self.model.objects.all()

    def get_templates_name():
        return self.template_name
'''

class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')

