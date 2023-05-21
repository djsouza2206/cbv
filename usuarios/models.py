from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    logradouro = models.CharField(max_length=255, null=True)
    nro = models.IntegerField(null=True, verbose_name="Número")
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Usuário")      # noqa : E501
