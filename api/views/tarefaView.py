from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importando modelo e serializer específicos:
from api.models.tarefaModel import TarefaModel  
from api.serializers.tarefaSerializer import TarefaSerializer 

class TarefaView(APIView):
      
     # Listar | Retorna a lista de todas as tarefas
    def get(self, request):
        # puxa todos os objetos do model tarefa
        tarefa = TarefaModel.objects.all() 
        # é possível puxar vários objetos
        serializer = TarefaSerializer(tarefa, many=True)
        # retorna todos os dados serializados JSON
        return Response(serializer.data)
        
    # Criar | Permite a criação de uma tarefaa nova
    def post(self, request):
        try:
            # recebe dados em JSON e os desserializa 
            serializer = TarefaSerializer(data=request.data)
            # se o JSON recebiido for válido, salvar
            if serializer.is_valid():
                serializer.save()
                # retorna mensagem juntamente com os dados atualizados
                return Response({      
                    "mensagem": "tarefa adicionada com sucesso!",
                    "dados atualizados": serializer.data
                }, status=status.HTTP_201_CREATED)
        except Exception as errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        

