from django.urls import path
from . import views
from .views import AgendaListView, AgendaCreateView, AgendaUpdateView, AgendaDeleteView

urlpatterns = [
    path('', AgendaListView.as_view(), name='lista'),
    path('cadastrar/', AgendaCreateView.as_view(), name='cadastrar'),
    path('atualizar/<int:pk>', AgendaUpdateView.as_view(), name='atualizar'),
    path('deletar/<int:pk>', AgendaDeleteView.as_view(), name='deletar'),
    path('person/json1/', views.cadastro_json1, name='cadastro_json1'),
]
