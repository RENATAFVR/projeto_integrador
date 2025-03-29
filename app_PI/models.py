
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, senha, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        
        email = self.normalize_email(email)
        usuario = self.model(nome=nome, email=email, **extra_fields)
        usuario.set_password(senha)  # Criptografa a senha
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome
