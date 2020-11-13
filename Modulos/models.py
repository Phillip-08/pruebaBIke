from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone

# Create your models here

class registro1(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.IntegerField(null=False, blank=False, primary_key=True)
    nombre_usario = models.CharField(max_length=20, blank= False, null= False)
    comuna = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField()
    password =models.CharField(max_length=20, blank= False, null= False)
    creacion_usr = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-rut']

    def __str__(self):
        return self.nombre

    


