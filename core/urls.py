from django.urls import path
from .views import hola_mundo, estudiante_list, crear_estudiante

urlpatterns = [
    path("", hola_mundo, name="hola"),
    path("listar-estudiante/", estudiante_list, name="listar-estudiantes"),
    path("crear-estudiante-model", crear_estudiante, name="crear-estudiante-model"),
]