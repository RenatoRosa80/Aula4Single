from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nome = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    idade = models.IntegerField()
    ativo = models.BooleanField(default=True)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=100)
    data_nascimento = models.DateTimeField()
    sexo = models.CharField(max_length=1)
    criado_em =  models.DateTimeField(auto_now_add=True)
    atualizado_em =  models.DateTimeField(auto_now_add=True)

