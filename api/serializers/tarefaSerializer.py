from rest_framework import serializers
 #classe de models em que o serializer está se relacionando
from api.models.tarefaModel import TarefaModel

class TarefaSerializer(serializers.ModelSerializer):
     class Meta:
        model = TarefaModel
        fields = '__all__'   #serializa todos os campos do modelo
