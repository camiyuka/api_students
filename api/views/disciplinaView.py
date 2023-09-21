from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.disciplinaModel import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaView(APIView):
    # Listagem de Disciplinas
    def get(self, request):
        disciplina = DisciplinaModel.objects.all()
        serializer = DisciplinaSerializer(disciplina, many=True)  
        return Response(serializer.data)

    #Criação de uma Disciplina:
    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_detail(self, request,pk):
        try:
            disciplina = DisciplinaModel.objects.get(pk=pk)
            serializer= DisciplinaSerializer(disciplina)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DisciplinaModel.DoesNotExist:
            return Response("disciplina não encontrada", status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)