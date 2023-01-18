from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    camada = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.camada}, {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(default=0)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"




class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(default=0)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(default=123)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(default=0)
    esta_aprobado = models.BooleanField(default=False)

# Create your models here.
