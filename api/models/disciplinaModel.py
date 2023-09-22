from django.db import models

# criação de uma disciplina com nome e descrição
class DisciplinaModel(models.Model):
    nome= models.CharField(max_length=50)
    descricao=models.CharField(max_length=100)
    