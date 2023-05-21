from django.urls import path
from .views import CampoCreate, AtividadeCreate, MunicipioCreate
from .views import CampoUpdate, AtividadeUpdate, MunicipioUpdate
from .views import CampoDelete, AtividadeDelete, MunicipioDelete
from .views import CampoList, AtividadeList, MunicipioList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),            # noqa : E501
    path('cadastrar/municipio/', MunicipioCreate.as_view(), name='cadastrar-municipio'),            # noqa : E501

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),         # noqa : E501
    path('editar/municipio/<int:pk>/', MunicipioUpdate.as_view(), name='editar-municipio'),         # noqa : E501

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),                   # noqa : E501
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),       # noqa : E501
    path('excluir/municipio/<int:pk>/', MunicipioDelete.as_view(), name='excluir-municipio'),       # noqa : E501

    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),                  # noqa : E501
    path('listar/municipios/', MunicipioList.as_view(), name='listar-municipios'),                  # noqa : E501
]
