from django.db import models
from negocios.models import Negocio

# Create your models here.
class Banner(models.Model):
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='banners/')
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)