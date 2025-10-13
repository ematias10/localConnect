from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.ImageField(upload_to='categorias/iconos/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre