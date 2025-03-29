from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm
from .models import Usuario
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request,'usuario/index.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])  # Criptografando a senha
            usuario.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, "Erro ao cadastrar usuário. Verifique os dados.")
    else:
        form = UsuarioForm()
    
    return render(request, 'usuario/cadastro.html', {'form': form})
 
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))

def login_usuario(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            usuario = authenticate(request, username=email, password=senha)

            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('dashboard')  # Redireciona para a área logada
            else:
                messages.error(request, "E-mail ou senha incorretos.")
    else:
        form = LoginForm()

    return render(request, "usuario/login.html", {"form": form})

def logout_usuario(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('login')
