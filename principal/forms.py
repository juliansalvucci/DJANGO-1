#formulario de django para crear contenido html según el modelo.

from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta: #indico modelo de referemcia
        model = Persona
        fields = '__all__' #Indico que uso todos los campos

        #(nombre,correo) para determinados campos.