from django.db import models

# criação de aluno, passando o nome e o e-mail
class AlunoModel(models.Model):
    nome= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)