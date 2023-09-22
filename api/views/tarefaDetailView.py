from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importando modelo e serializer específicos:
from api.models.tarefaModel import TarefaModel  
from api.serializers.tarefaSerializer import TarefaSerializer

class TarefaDetailView(APIView):
    def get (self, request,pk):
        try:
            # pegar tarefa de acordo com OK
            tarefa = TarefaModel.objects.get(pk=pk)
            serializer= TarefaSerializer(tarefa)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TarefaModel.DoesNotExist:
            # se ela não existir, mensagem "tarefa não encontrada"
            return Response("tarefa não encontrada", status=status.HTTP_404_NOT_FOUND)
        # tratamento de excessão com mensagem
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        
        # editar tarefa
    def put(self, request, pk):
        try:
            tarefa=TarefaModel.objects.get(pk=pk)
             # é possível realizar mudanças em apenas algumas partes do objeto
            serializer = TarefaSerializer(tarefa, data= request.data, partial=True)
            if(serializer.is_valid()):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # tratamento de exceção com o erro
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
            
    # deleta tarefa
    def delete(self, request, pk):
        # deleta tarefa
        try:
            tarefa = TarefaModel.objects.get(pk=pk)
            tarefa.delete()
            # se der certo, exibe a mensagem de sucesso "tarefa deletada com sucesso!"
            return Response("tarefa deletada com sucesso!",status= status.HTTP_204_NO_CONTENT)
            # se não encontrar, mensagem "tarefa não encontrada"
        except TarefaModel.DoesNotExist:
                return Response("tarefa não encontrada", status=status.HTTP_404_NOT_FOUND)
        
    