from rest_framework import serializers
from api.models.tarefaModel import TarefaModel

class TarefaSerializer(serializers.ModelSerializer):
     class Meta:
        model = TarefaModel
        fields = '__all__'  # Use a list or tuple, not parentheses