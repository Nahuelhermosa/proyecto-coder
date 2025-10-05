from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ["username", "email", "avatar", "password1", "password2"]
        help_texts = {
            "username": None,
            "password1": None,
            "password2": None
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "avatar", "bio", "first_name", "last_name"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"})
        }