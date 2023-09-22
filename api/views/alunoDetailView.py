
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importando modelo e serializer específicos:
from api.models.alunoModel import AlunoModel  
from api.serializers.alunoSerializer import AlunoSerializer 

# nessa classe, todas as funções puxam apenas um objeto pela PK (diferentemente da aluno view)
class AlunoDetailView(APIView):
    # detalhar| Retorna detalhes de um aluno específico com base no id
    def get(self, request,pk):
        try:
             #puxa o aluno pela sua PK
            alunos = AlunoModel.objects.get(pk=pk)
            serializer= AlunoSerializer(alunos)
            #se encontrar, retornará JSON de aluno
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except AlunoModel.DoesNotExist:
             #se o aluno não for encontrado, aparecerá mensagem "aluno não encontrado"
            return Response("aluno não encontrado", status=status.HTTP_404_NOT_FOUND)
        # taratemnto de excessão retorna erro 400 
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST) ##

    # atualizar |  permite a atualização dos detalhes de um aluno específico com base no id                            
    def put(self, request, pk):
        try:
            alunos=AlunoModel.objects.get(pk=pk)
            # partial= True define que é possível alterar apenas alguns campos do objeto, não necessariamente todos
            serializer = AlunoSerializer(alunos, data= request.data, partial=True)
            if(serializer.is_valid()):
                serializer.save()
                return Response({
                    # retorna mensagem juntamente com os dados atualizados
                "message": "aluno atualizado com sucesso!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
            #excessão retorna mensagem de erro
        except Exception as e:
            return Response({
            "error": "Erro ao atualizar aluno",
            "details": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

    # excluir | Permite a exclusão de um aluno específico com base no id. Além disso, todas as tarefas associadas a esse aluno são excluídas ou desassociadas.      

    def delete(self, request, pk):
        try:
            #encontra o aluno pela pk
            alunos = AlunoModel.objects.get(pk=pk)
            #deleta aluno
            alunos.delete()
            # mensagem que aparece:
            return Response( "aluno deletado com sucesso!",status= status.HTTP_204_NO_CONTENT)
        except AlunoModel.DoesNotExist:
            # se não encontrar aluno:
            return Response("aluno não encontrado", status=status.HTTP_404_NOT_FOUND)
    
