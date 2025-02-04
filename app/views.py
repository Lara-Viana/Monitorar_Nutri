from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class TreinoView(View):
    def get(self,request):
        contexto = {
            'treino': Treino.objects.all(),
        }
        return render(request, 'treino.html', contexto)

class DietaView(View):
    def get(self,request):
        contexto = {
            'dieta': Dieta.objects.all(),
        }
        return render(request, 'dieta.html', contexto)  
    
class CategoriaView(View):
    def get(self,request):
        contexto = {
            'categoria': CategoriaAlimento.objects.all(),
        }
        return render(request, 'categoria.html', contexto)  
    
class PacienteView(View):
    def get(self,request):
        contexto = {
            'paciente': Paciente.objects.all(),
        }
        return render(request, 'paciente.html', contexto)  
    
class AlimentoView(View):
    def get(self,request):
        contexto = {
            'alimento': Alimento.objects.all(),
        }
        return render(request, 'alimento.html', contexto)  
    
class RefeicaoView(View):
    def get(self,request):
        contexto = {
            'refeicao': Refeicao.objects.all(),
        }
        return render(request, 'refeicao.html', contexto)  
    
class AtivFisView(View):
    def get(self,request):
        contexto = {
            'ativfis': AtividadeFisica.objects.all(),
        }
        return render(request, 'ativfis.html', contexto)  
    
class UniMedView(View):
    def get(self,request):
        contexto = {
            'unimed': UnidadeMedida.objects.all(),
        }
        return render(request, 'unimed.html', contexto)  


# Create your views here.