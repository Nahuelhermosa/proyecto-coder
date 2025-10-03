from django.db import models
import random

def obtener_numero_random():
    random_nro = random.randint(1000, 9999)
    
    from .models import Curso  
    if not Curso.objects.filter(numero_curso=random_nro).exists():
        return random_nro
    return obtener_numero_random()

from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)  # ✅
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"