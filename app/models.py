from django.db import models

# RF01 - Gerenciar Categoria Alimento
class CategoriaAlimento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# RF02 - Gerenciar Unidade Medida
class UnidadeMedida(models.Model):
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.sigla

# RF03 - Gerenciar Pacientes
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.FloatField()
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nasc = models.DateField()
    objetivo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

# RF04 - Gerenciar Alimento
class Alimento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaAlimento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

# RF05 - Gerenciar Refeição
class Refeicao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# RF06 - Gerenciar Atividades Físicas
class AtividadeFisica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# RF07 - Gerenciar Dietas
class Dieta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    medida = models.FloatField()
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)
    refeicoes_livres = models.FloatField()

    def __str__(self):
        return f"Dieta de {self.paciente} - {self.refeicao}"

# RF08 - Gerenciar Treinos
class Treino(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    atividade_fisica = models.ForeignKey(AtividadeFisica, on_delete=models.CASCADE)
    duracao = models.PositiveIntegerField(help_text="Duração em minutos")

    def __str__(self):
        return f"Treino de {self.paciente} - {self.atividade_fisica}"