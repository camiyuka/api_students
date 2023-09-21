from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from api.models.alunoModel import AlunoModel  
from api.serializers.alunoSerializer import AlunoSerializer 

class AlunoView(APIView):
      
     # Listar | Retorna a lista de todos os alunos
    def get(self, request):
        alunos = AlunoModel.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
        
    # Criar | Permite a criação de um novo aluno.
    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

