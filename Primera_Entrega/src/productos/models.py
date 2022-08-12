from django.db import models



# Create your models here.
class Vegetales(models.Model):
    nombre =models.CharField(max_length=50)
    cosecha = models.DateField(blank=True, null=True)
    precio = models.FloatField()
    
    
    def __str__(self):
        return f"{self.nombre}"
    
class NoPerecederos(models.Model):
    nombre =models.CharField(max_length=50)
    precio = models.FloatField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    
class Perecederos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    precio = models.FloatField()
    def __str__(self):
        return f"{self.nombre}"