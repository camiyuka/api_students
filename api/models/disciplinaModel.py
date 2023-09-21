from django.db import models

class DisciplinaModel(models.Model):
    nome= models.CharField(max_length=50)
    descricao=models.CharField(max_length=100)
    