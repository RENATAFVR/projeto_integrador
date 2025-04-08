from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cep', 'logradouro', 'numero', 'bairro', 'cidade', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
        }
