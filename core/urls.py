from django.urls import path
from .views import estudiante_list, crear_estudiante, crear_profesor, listar_profesores, listar_cursos, crear_curso, index, editar_estudiante,eliminar_estudiante,estudiante_detail

urlpatterns = [
    path("", index, name="index"),
    path("listar-estudiante/", estudiante_list, name="listar-estudiantes"),
    path("crear-estudiante-model", crear_estudiante, name="crear-estudiante-model"),
    path("profesores-crear/", crear_profesor, name="crear-profesor"),
    path("listar-profesores/", listar_profesores, name="listar-profesores"),
    path("listar-cursos/", listar_cursos, name="listar-cursos"),
    path("cursos/crear/", crear_curso, name="crear-curso"),
    path("estudiantes/<int:estudiante_id>/editar/", editar_estudiante, name="editar-estudiante"),
    path("estudiantes/<int:estudiante_id>/eliminar/", eliminar_estudiante, name="eliminar-estudiante"),
    path("estudiante-detalle/<int:pk>/", estudiante_detail, name="detalle-estudiante")
    
]
