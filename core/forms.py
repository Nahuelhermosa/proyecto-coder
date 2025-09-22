from django import forms
from core.models import estudiante,Curso, Profesor


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = estudiante
        fields = ["nombre", "apellido", "nro_legajo", "email", "fecha_nacimiento"]
        # exclude = ["..."]
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"})
        }
        error_messages = {
            "nro_legajo": {
                "unique": "Numero de legajo existente",
            }
        }
    

class EstudianteFormManual(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Correo electronico")
    nro_legajo = forms.IntegerField(label="Nro de legajo")
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Fecha de nacimiento"
    )
    
    def clean_nro_legajo(self):
        nro_legajo = self.cleaned_data["nro_legajo"]
        if estudiante.objects.filter(nro_legajo=nro_legajo).exists():
            raise forms.ValidationError("Numero de legajo existente")
        return nro_legajo
    
    
# Formulario Curso
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre", "codigo", "descripcion", "fecha_inicio", "fecha_fin"]
        labels = {
            "nombre": "Nombre del curso",
            "codigo": "Código",
            "descripcion": "Descripción",
            "fecha_inicio": "Fecha de inicio",
            "fecha_fin": "Fecha de fin",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

# Formulario Profesor
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'especialidad', 'cursos']
        
        labels = {
            "nombre": "Nombre del Profesor",
            "apellido": "Apellido",
            "email": "Correo Electrónico",
            "materia": "Materia que dicta",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "materia": forms.TextInput(attrs={"class": "form-control"}),
        }


# Formulario de busqueda
class BuscarEstudianteForm(forms.Form):
    apellido = forms.CharField(max_length=50, label="Buscar por apellido")