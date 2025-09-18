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
    
    
# Formulario para Curso
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'descripcion', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'})
        }

# Formulario para Profesor
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'especialidad', 'cursos']
        widgets = {
            'cursos': forms.CheckboxSelectMultiple()  # Para seleccionar varios cursos
        }

# Formulario de búsqueda (por ejemplo, Estudiante por apellido)
class BuscarEstudianteForm(forms.Form):
    apellido = forms.CharField(max_length=50, label="Buscar por apellido")