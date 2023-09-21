from django.db import models

class AlunoModel(models.Model):
    nome= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)