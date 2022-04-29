from django.db import models

# Create your models here.

class Producto(models.Model):
    imagen = models.FileField(upload_to="")
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()

    class Meta:
        db_table = "computador"
