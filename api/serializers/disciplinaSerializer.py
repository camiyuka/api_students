from rest_framework import serializers
from api.models.disciplinaModel import DisciplinaModel

class DisciplinaSerializer(serializers.ModelSerializer):
     class Meta:
        model = DisciplinaModel
        fields = '__all__' 
