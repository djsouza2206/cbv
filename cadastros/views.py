from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Campo, Atividade, Municipio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404


# ############ CREATE VIEW #############

class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):                          # noqa : E501
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastrar-campo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastrar Campo'
        context['botao'] = 'Cadastrar'
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        # CASO QUEIRA ENVIAR MAIS ALGUM DADO EM ALGUM CAMPO QUE NÃO SEJA OBRIGATÓRIO            # noqa : E501
        # self.object.descricao += " TESTE"
        # self.object.save()
        return url


class AtividadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo', 'arquivo']
    template_name = 'cadastros/form_atividade.html'
    success_url = reverse_lazy('cadastrar-atividade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastrar Atividade'
        context['botao'] = 'Cadastrar'
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        # CASO QUEIRA ENVIAR MAIS ALGUM DADO EM ALGUM CAMPO QUE NÃO SEJA OBRIGATÓRIO            # noqa : E501
        # self.object.descricao += " TESTE"
        # self.object.save()
        return url


class MunicipioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):                          # noqa : E501
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Municipio
    fields = ['uf', 'cod_uf', 'cod_munic', 'municipio', 'populacao', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastrar-municipio')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastrar Município'
        context['botao'] = 'Cadastrar'
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        # CASO QUEIRA ENVIAR MAIS ALGUM DADO EM ALGUM CAMPO QUE NÃO SEJA OBRIGATÓRIO            # noqa : E501
        # self.object.descricao += " TESTE"
        # self.object.save()
        return url

# ############ UPDATE VIEW #############


class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alterar Campo'
        context['botao'] = 'Alterar'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'],usuario=self.request.user)                      # noqa : E501 
        # self.object = Campo.objects.get(pk=self.kwargs['pk'],usuario=self.request.user)  ACIMA JEITO ELEGANTE     # noqa : E501
        return self.object


class AtividadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alterar Atividade'
        context['botao'] = 'Alterar'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'],usuario=self.request.user)                  # noqa : E501
        # self.object = Atividade.objects.get(pk=self.kwargs['pk'],usuario=self.request.user)                       # noqa : E501
        return self.object


class MunicipioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Municipio
    fields = ['uf', 'cod_uf', 'cod_munic', 'municipio', 'populacao', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-municipios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alterar Município'
        context['botao'] = 'Alterar'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Municipio, pk=self.kwargs['pk'],usuario=self.request.user)                  # noqa : E501 
        # self.object = Campo.objects.get(pk=self.kwargs['pk'],usuario=self.request.user)  ACIMA JEITO ELEGANTE     # noqa : E501
        return self.object


# ############ DELETE VIEW #############


class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Excluir Campo'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Campo, pk=self.kwargs['pk'],usuario=self.request.user)                      # noqa : E501     
        return self.object


class AtividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Excluir Atividade'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'],usuario=self.request.user)                      # noqa : E501     
        return self.object


class MunicipioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Municipio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-municipios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Excluir Município'
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Municipio, pk=self.kwargs['pk'],usuario=self.request.user)                      # noqa : E501     
        return self.object


# ############ LIST VIEW #############
class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

    def get_queryset(self):
        self.object_list = Campo.objects.filter(usuario=self.request.user)
        return self.object_list


class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

    def get_queryset(self):
        self.object_list = Atividade.objects.filter(usuario=self.request.user)
        return self.object_list


class MunicipioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Municipio
    template_name = 'cadastros/listas/municipio.html'
    paginate_by = 10

    def get_queryset(self):
        busca = self.request.GET.get('nome')

        if busca:
            municipios = Municipio.objects.filter(municipio__icontains=busca,usuario=self.request.user)         # noqa : E501            
        else:
            municipios = Municipio.objects.filter(usuario=self.request.user)                            # noqa : E501

        return municipios
