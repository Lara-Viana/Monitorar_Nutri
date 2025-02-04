from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dieta/', DietaView.as_view(), name='dieta'),
    path('treino/', TreinoView.as_view(), name='treino'),
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('categoria/', CategoriaView.as_view(), name='categoria'),
    path('unimed/', UniMedView.as_view(), name='unimed'),
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('alimento/', AlimentoView.as_view(), name='alimento'),
    path('refeicao/', RefeicaoView.as_view(), name='refeicao'),
    path('ativfis/', AtivFisView.as_view(), name='ativfis'),
]