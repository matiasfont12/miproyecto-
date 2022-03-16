from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)


class Curso(models.Model):
    nombre = models.CharField(max_length=10)
    curso = models.IntegerField()


class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_de_entrega = models.DateTimeField()
    entregado = models.BooleanField()

  
