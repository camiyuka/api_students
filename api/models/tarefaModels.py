from django.db import models
from api.models.alunoModel import AlunoModel
from api.models.disciplinaModel import DisciplinaModel

class TarefaModel(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)
    
    aluno = models.ForeignKey(AlunoModel, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(DisciplinaModel)