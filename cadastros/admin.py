from django.contrib import admin
from .models import Campo, Atividade


@admin.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descricao', 'pontos',
                    'detalhes', 'campo', 'usuario')
