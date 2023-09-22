from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importando modelo e serializer específicos:
from api.models.tarefaModel import TarefaModel
from api.serializers.tarefaSerializer import TarefaSerializer

#lista as tarefas de um aluno específico com base no aluno fornecido como parâmetro

class TarefaPorAlunoView(APIView):
        def get(self, request, aluno , format= None):
            try: 
                tarefa=  TarefaModel.objects.filter(aluno=aluno)
                # é possível puxar vários alunos
                serializer= TarefaSerializer(tarefa, many=True)
                # retorna os dados serializados em JSON 
                return Response(serializer.data)
            #tratamento de exceção com mensagem de erro
            except Exception as e:
                return Response ({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)