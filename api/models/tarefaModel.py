from django.db import models
from api.models.alunoModel import AlunoModel
from api.models.disciplinaModel import DisciplinaModel

# criação de tarefa, com título, descrição e disciplina
class TarefaModel(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)

    # aluno está associado a tarefa, se aluno for excluído, essa tarefa também será
    aluno = models.ForeignKey(AlunoModel, on_delete=models.CASCADE)

    # várias disciplinas estão associadas a essa tarefa
    disciplinas = models.ManyToManyField(DisciplinaModel)   