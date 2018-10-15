from django.urls import path
from . import views
from .views import AgendaListView, CadastroCreateView, AgendaUpdateView, AgendaDeleteView

urlpatterns = [
    path('', AgendaListView.as_view(), name='lista'),
    path('cadastrar/', CadastroCreateView.as_view(), name='cadastrar'),
    path('atualizar/<pk>', AgendaUpdateView.as_view(), name='atualizar'),
    path('deletar/<pk>', AgendaDeleteView.as_view(), name='deletar'),
    path('person/json/', views.cadastro_json, name='cadastro_json'),
]
