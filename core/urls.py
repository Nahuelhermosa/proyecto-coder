from django.urls import path
from .views import hola_mundo, estudiante_list, crear_estudiante, crear_profesor, listar_profesores, listar_cursos,crear_curso

urlpatterns = [
    path("", hola_mundo, name="hola"),
    path("listar-estudiante/", estudiante_list, name="listar-estudiantes"),
    path("crear-estudiante-model", crear_estudiante, name="crear-estudiante-model"),
    path("profesores-crear/", crear_profesor, name="crear-profesor"),
    path("listar-profesores/", listar_profesores, name="listar-profesores"),
    path("listar-cursos/", listar_cursos, name="listar-cursos"),
    path("cursos/crear/", crear_curso, name="crear-curso"),
]
