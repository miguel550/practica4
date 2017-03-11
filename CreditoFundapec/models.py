from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    matricula = models.CharField(max_length=8, unique=True)


class Credito(models.Model):
    estudiante = models.OneToOneField(Estudiante)
    monto = models.DecimalField(decimal_places=2, max_digits=10)
    fecha_inicio = models.DateTimeField(auto_now_add=True)


class Transaccion(models.Model):
    credito = models.ForeignKey(Credito)
    monto = models.DecimalField(decimal_places=2, max_digits=10)
    fecha = models.DateTimeField(auto_now_add=True)
