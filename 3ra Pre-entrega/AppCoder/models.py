from django.db import models

# Create your models here.

class Perros (models.Model): #herencia. No siempre se hereda de models.model, es la manera generica de Django pero hay otras maneras.
    producto = models.CharField(max_length=30)

class Gatos (models.Model): 
    producto = models.CharField(max_length=30)

class Peces (models.Model): 
    producto = models.CharField(max_length=30)

class Compra (models.Model):

    def __str__(self):

        return f"Producto: {self.producto} | | | Número: {self.numero}"

    producto = models.CharField(max_length=30)
    numero = models.IntegerField()