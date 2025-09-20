from django.shortcuts import render, redirect
# from .models import Estudiante # Relativa
from core.models import estudiante# Absoluta
from core.forms import EstudianteForm, EstudianteFormManual, ProfesorForm
from .models import Profesor
# Create your views here.
# dict.items() -> dict_items([(k1, v1), (k2, v2), ...])
def hola_mundo(request):
    return render(request, "core/index.html")

# def estudiante_list(request):
#     # Lógica para obtener la lista de estudiantes desde la base de datos
#     estudiantes = Estudiante.objects.all() # QuerySet([<Estudiante>, <Estudiante>, ...])
#     #estudiantes = Estudiante.objects.filter(nombre__startswith="F") # QuerySet([<Estudiante>, <Estudiante>, ...])
#     # Estudiante.objects.filter(nombre__startswith="A", edad__gte=15) # AND
#     contexto = {
#         "lista_estudiantes": estudiantes
#     }
#     return render(request, "core/estudiantes_list.html", contexto)

# POST - Crear info / GET - Pedir info / DELETE = Eliminar / PUT,UPDATE = Editar
def crear_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("listar-estudiantes")
    else:
        formulario = EstudianteForm()

    return render(request, "core/estudiante_form.html", {"form": formulario})


def estudiante_list(request):
    query = request.GET.get("q", "")
    
    if query:
        lista_estudiantes =estudiante.objects.filter(nombre__icontains=query)
    else:
        lista_estudiantes = estudiante.objects.all()
    
    contexto = {
        "lista_estudiantes": lista_estudiantes
    }
    return render(request, "core/estudiantes_list.html", contexto)

def crear_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar-profesores")  # Redirige a la lista de profesores
    else:
        form = ProfesorForm()
    
    return render(request, "core/profesores_list.html", {"form": form})


def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "core/profesores.html", {"profesores": profesores})

