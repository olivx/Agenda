from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CadastroForm
from .models import Cadastro
from django.http import JsonResponse


class AgendaCreateView(CreateView):
    form_class = CadastroForm
    template_name = "cadastrar.html"
    model = Cadastro
    success_url = reverse_lazy("lista")


class AgendaListView(ListView):
    template_name = "lista.html"
    model = Cadastro
    context_object_name = "cadastros"
    query_results = Cadastro.objects.all()


class AgendaUpdateView(UpdateView):
    form_class = CadastroForm
    template_name = "atualizar.html"
    model = Cadastro
    success_url = reverse_lazy("lista")


class AgendaDeleteView(DeleteView):
    form_class = CadastroForm
    template_name = "deletar.html"
    model = Cadastro
    context_object_name = "deletar"
    success_url = reverse_lazy("lista")


def cadastro_json1(request):
    cadastros = Cadastro.objects.all()
    data = [cadastro.to_dict_json() for cadastro in cadastros]
    response = {'data': data}
    return JsonResponse(response)
