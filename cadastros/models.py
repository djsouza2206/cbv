from django.db import models
from django.contrib.auth.models import User


class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Campo'
        verbose_name_plural = 'Campos'

    def __str__(self):
        return "{} - {}".format(self.nome, self.descricao)


class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name="Descricão")
    pontos = models.DecimalField(max_digits=4, decimal_places=1)
    detalhes = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to="pdf/", null=False, blank=True)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return "{} - {}".format(self.numero, self.descricao)
