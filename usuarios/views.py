from django.views.generic.edit import CreateView, UpdateView
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from .models import Perfil


class UsuarioCreate(CreateView):
    template_name = 'cadastros/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Colaborador")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registrar Usuário'
        context['botao'] = 'Registrar'
        return context


class PerfilUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Perfil
    fields = ['nome_completo', 'cpf', 'logradouro', 'nro', 'telefone']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastrar Usuário'
        context['botao'] = 'Cadastrar'
        return context
