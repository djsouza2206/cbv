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


ESTADOS_BRASILEIROS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)


class Municipio(models.Model):
    uf = models.CharField(max_length=2, choices=ESTADOS_BRASILEIROS, verbose_name="UF")                # noqa : E501
    cod_uf = models.IntegerField(max_length=2, verbose_name="Cód UF")
    cod_munic = models.CharField(max_length=5, verbose_name="Cód Munic")
    municipio = models.CharField(max_length=100, verbose_name="Município")
    populacao = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="População")         # noqa : E501

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

    def __str__(self):
        return "{} - {}".format(self.uf, self.municipio)
