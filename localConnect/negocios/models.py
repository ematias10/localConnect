from django.db import models
from suscripciones.models import NivelSuscripcion
from usuarios.models import Usuario
from categorias.models import Categoria

# Create your models here.
class Negocio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    redess_sociales = models.JSONField(blank=True, null=True)
    banner_activo = models.BooleanField(default=False)
    publicado = models.BooleanField(default=False)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    nivel_suscripcion = models.ForeignKey(NivelSuscripcion, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.nombre