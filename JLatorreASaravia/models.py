from django.db import models
# Create your models here.
class Compra(models.Model):
    Rut = models.CharField (max_length=30 ,)
    Producto = models.CharField(max_length=30)
    Cantidad = models.CharField(max_length=25,)
    Iva = models.DecimalField(max_digits=30, decimal_places=2)
    Valor_Venta = models.DecimalField(max_digits=30, decimal_places=2)
    Total = models.DecimalField(max_digits=30, decimal_places=2)
    
def __str__(self):
    return self.Nombre