from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


class ContatoView(TemplateView):
    template_name = 'core/contato.html'
