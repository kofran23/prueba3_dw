from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.CharField(max_length=10)

class Casas(models.Model):
    ciudad=models.CharField(max_length=30)
    medidas=models.CharField(max_length=50)
    categoria=models.CharField(max_length=100)
    precio=models.IntegerField()

class Compra(models.Model):
    pago=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()    
