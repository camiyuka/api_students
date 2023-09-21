
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.alunoModel import AlunoModel  
from api.serializers.alunoSerializer import AlunoSerializer 

class AlunoDetailView(APIView):

    # detalhar| Retorna detalhes de um aluno específico com base no id
    def get(self, id):
        try:
            alunos = AlunoModel.objects.get(pk=id)
            serializer= AlunoSerializer(alunos)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AlunoModel.DoesNotExist:
            return Response("aluno não encontrado", status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)

    # atualizar |  permite a atualização dos detalhes de um aluno específico com base no id                            
    def put(self, id):
        try:
            alunos=AlunoModel.objects.get(pk=id)
            serializer = AlunoSerializer(alunos, data= alunos.data, partial=True)
            if(serializer.is_valid()):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # excluir | Permite a exclusão de um aluno específico com base no id. Além disso, todas as tarefas associadas a esse aluno devem ser excluídas ou desassociadas.      

    def delete(self, id):
        try:
            alunos = AlunoModel.objects.get(pk=id)
            alunos.delete()
            return Response( "aluno deletado com sucesso!",status= status.HTTP_204_NO_CONTENT)
        except AlunoModel.DoesNotExist:
            return Response("aluno não encontrado", status=status.HTTP_404_NOT_FOUND)
    