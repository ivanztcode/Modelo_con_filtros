from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Producto" , max_length=50)
    descripcion = models.TextField(verbose_name="Descripción del producto")
    precio = models.DecimalField(verbose_name="Precio del producto" ,max_digits=7, decimal_places=2)
    cantidad = models.IntegerField(verbose_name="Stock")
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre