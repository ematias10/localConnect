from django.db import models

# Create your models here.
class Usuario(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('profesional', 'Profesional'),
    )
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_usuario