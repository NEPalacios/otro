from django.db import models


# Create your models here.
  

class Producto(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.nombre + ", $" + str(self.precio) + ", " + self.descripcion