from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.tarefaModel import TarefaModel  
from api.serializers.tarefaSerializer import TarefaSerializer

class TarefaDetailView(APIView):
    def get (self, request,pk):
        try:
            tarefa = TarefaModel.objects.get(pk=pk)
            serializer= TarefaSerializer(tarefa)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TarefaModel.DoesNotExist:
            return Response("tarefa não encontrada", status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
    #  try:
        tarefa=TarefaModel.objects.get(pk=pk)
        serializer = TarefaSerializer(tarefa, data= request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        try:
            tarefa = TarefaModel.objects.get(pk=pk)
            tarefa.delete()
            return Response( "tarefa deletada com sucesso!",status= status.HTTP_204_NO_CONTENT)
        except TarefaModel.DoesNotExist:
                return Response("tarefa não encontrada", status=status.HTTP_404_NOT_FOUND)