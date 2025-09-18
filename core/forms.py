from django import forms
from core.models import estudiante


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
        if Estudiante.objects.filter(nro_legajo=nro_legajo).exists():
            raise forms.ValidationError("Numero de legajo existente")
        return nro_legajo