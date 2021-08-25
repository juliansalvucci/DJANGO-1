from django.db import models

#Modelo que representa tabla en la base de datos.

class Persona(models.Model): #campo autoincremental
    id = models.AutoField(
        primary_key=True   #asigna como clave primaria
    ) 
    nombre = models.CharField(
        max_length=100,
        unique=True #No permite agregar valores repetidos
    )
    apellido = models.CharField(
        max_length=200
    )
    correo = models.EmailField(
        max_length=200
    )

    def __str__(self):  #Muestra el nombre del objeto en lugar de object
        return self.nombre
