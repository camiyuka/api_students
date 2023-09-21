from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.tarefaModel import TarefaModel  
from api.serializers.tarefaSerializer import TarefaSerializer 

class TarefaView(APIView):
      
     # Listar | Retorna a lista de todas as tarefas
    def get(self, request):
        tarefa = TarefaModel.objects.all() 
        serializer = TarefaSerializer(tarefa, many=True)
        return Response(serializer.data)
        
    # Criar | Permite a criação de uma tarefaa nova
    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

