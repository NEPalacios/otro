from django.db import models


# Create your models here.
  

class Producto(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.nombre + ", $" + str(self.precio) + ", " + self.descripcion
    
# class Alta(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()

#     def __str__(self):
#         return str(self.producto) + " " + str(self.cantidad) 
    
# class Baja(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()

#     def __str__(self):
#         return str(self.producto) + " " + str(self.cantidad)

# class Modificacion(models.Model):   
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()

#     def __str__(self):
#         return str(self.producto) + " " + str(self.cantidad)