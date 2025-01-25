from django.db import models

# Create your models here.

class Universidad(models.Model):
    nombre = models.CharField(max_length= 30)
    pais = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    id_estudiante = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Envio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField() 
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()       
    def __str__(self):
        return f"{self.nombre} - Entregado: {'Sí' if self.entregado else 'No'}"


