from rest_framework import serializers
 #classe de models em que o serializer está se relacionando
from api.models.disciplinaModel import DisciplinaModel

class DisciplinaSerializer(serializers.ModelSerializer):
     class Meta:
        model = DisciplinaModel
        fields = '__all__'   #serializa todos os campos do modelo
