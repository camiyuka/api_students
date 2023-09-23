from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importando modelo e serializer específicos:
from api.models.disciplinaModel import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaView(APIView):
    # listagem de todas as disciplinas
    def get(self, request):
        disciplina = DisciplinaModel.objects.all()
        #pega vários objetos 
        serializer = DisciplinaSerializer(disciplina, many=True)  
        return Response(serializer.data)

    #Criação de uma Disciplina:
    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   