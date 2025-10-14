from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from cursosverano.models import Curso
from django.db.models import Q

class CursoListView(ListView):
    model = Curso
    template_name = "cursosverano/curso_list.html"
    context_object_name = "lista_curso"

    def get_queryset(self):
        queryset = Curso.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) | Q(codigo__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        return context


class CursoDetailView(DetailView):
    model = Curso
    template_name = "cursosverano/curso_detail.html"
    context_object_name = "curso"
    slug_field = "codigo"
    slug_url_kwarg = "codigo"


class CursoCreateView(CreateView):
    model = Curso
    fields = ["nombre", "codigo", "descripcion"]
    template_name = "cursosverano/curso_form.html"
    success_url = reverse_lazy("cursosverano:listar-cursos")


class CursoUpdateView(UpdateView):
    model = Curso
    fields = ["nombre", "codigo", "descripcion"]
    template_name = "cursosverano/curso_form.html"
    slug_field = "codigo"
    slug_url_kwarg = "codigo"
    success_url = reverse_lazy("cursosverano:listar-cursos")


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "cursosverano/curso_confirm_delete.html"
    slug_field = "codigo"
    slug_url_kwarg = "codigo"
    success_url = reverse_lazy("cursosverano:listar-cursos")
