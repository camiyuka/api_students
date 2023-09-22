from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.tarefaModel import TarefaModel
from api.serializers.tarefaSerializer import TarefaSerializer


class TarefaPorAlunoView(APIView):
        def get(self, request, aluno , format= None):
            try: 
                tarefa=  TarefaModel.objects.filter(aluno=aluno)
                serializer= TarefaSerializer(tarefa, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response ({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)