from rest_framework import serializers
 #classe de models em que o serializer está se relacionando
from api.models.alunoModel import AlunoModel

class AlunoSerializer(serializers.ModelSerializer):
     class Meta:
        model = AlunoModel
        fields = '__all__' #serializa todos os campos do modelo