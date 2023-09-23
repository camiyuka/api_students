from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importando modelo e serializer específicos:
from api.models.alunoModel import AlunoModel  
from api.serializers.alunoSerializer import AlunoSerializer 

class AlunoView(APIView):
      
     # Listar | Retorna a lista de todos os alunos
    def get(self, request):
        try:
            alunos = AlunoModel.objects.all() #aqui define todos os alunos
            serializer = AlunoSerializer(alunos, many=True) # serializa uma lista de objetos 
            return Response(serializer.data) # retorna todos os alunos 
        except:
            return Response("erro ao encontrar alunos", status=status.HTTP_400_BAD_REQUEST)
        
    # Criar | Permite a criação de um novo aluno.
    def post(self, request):
        try:
            serializer = AlunoSerializer(data=request.data) #pega os dados fornecidos e desserializa
            # se for válido, salva
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response("erro ao cadastrar aluno", status=status.HTTP_404_NOT_FOUND)

