from django.contrib import admin
from .models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'logradouro', 'nro', 'telefone', 'usuario')         # noqa : E501
