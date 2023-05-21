from django.contrib import admin
from .models import Campo, Atividade, Municipio


@admin.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descricao', 'pontos', 'detalhes', 'campo', 'usuario')            # noqa : E501


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('uf', 'cod_uf', 'cod_munic', 'municipio', 'populacao', 'usuario')           # noqa : E501
