from django.contrib import admin
from .models import (
    CategoriaAlimento, UnidadeMedida, Paciente, Alimento,
    Refeicao, AtividadeFisica, Dieta, Treino
)

# RF01 - Gerenciar Categoria Alimento
@admin.register(CategoriaAlimento)
class CategoriaAlimentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# RF02 - Gerenciar Unidade Medida
@admin.register(UnidadeMedida)
class UnidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ('sigla',)

# RF03 - Gerenciar Pacientes
class DietaInline(admin.TabularInline):  # Inline para Dieta
    model = Dieta
    extra = 1
    fields = ('refeicao', 'alimento', 'medida', 'unidade_medida', 'refeicoes_livres')  # Campos exibidos no inline

class TreinoInline(admin.TabularInline):  # Inline para Treino
    model = Treino
    extra = 1
    fields = ('atividade_fisica', 'duracao')  # Campos exibidos no inline

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'peso', 'sexo', 'data_nasc', 'objetivo')
    inlines = [DietaInline, TreinoInline]  # Inlines para Dieta e Treino

# RF04 - Gerenciar Alimento
@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')

# RF05 - Gerenciar Refeição
@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# RF06 - Gerenciar Atividades Físicas
@admin.register(AtividadeFisica)
class AtividadeFisicaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# RF07 - Gerenciar Dietas
@admin.register(Dieta)
class DietaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'refeicao', 'alimento', 'medida', 'unidade_medida', 'refeicoes_livres')

# RF08 - Gerenciar Treinos
@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'atividade_fisica', 'duracao')