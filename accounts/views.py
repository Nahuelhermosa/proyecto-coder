from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, LoginUserForm, CustomUserEditForm


def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Registro exitoso")
            return redirect("index")
        else:
            print(form.errors)  # <--- aquí
    else:
        form = RegistroUsuarioForm()
    return render(request, "accounts/registro.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserEditForm(instance=request.user)
    
    return render(request, "accounts/profile.html", {"form": form})