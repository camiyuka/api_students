from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.disciplinaModel import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaDetailView(APIView):
    def get (self, request,pk):
        try:
            disciplina = DisciplinaModel.objects.get(pk=pk)
            serializer= DisciplinaSerializer(disciplina)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DisciplinaModel.DoesNotExist:
            return Response("disciplina não encontrada", status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
    #  try:
        disciplina=DisciplinaModel.objects.get(pk=pk)
        serializer = DisciplinaSerializer(disciplina, data= request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        try:
            disciplina = DisciplinaModel.objects.get(pk=pk)
            disciplina.delete()
            return Response( "disciplina deletada com sucesso!",status= status.HTTP_204_NO_CONTENT)
        except DisciplinaModel.DoesNotExist:
                return Response("disciplina não encontrada", status=status.HTTP_404_NOT_FOUND)