from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importando modelo e serializer específicos:

from api.models.disciplinaModel import DisciplinaModel
from api.serializers.disciplinaSerializer import DisciplinaSerializer

# nessa classe, todas as funções puxam apenas um objeto pela PK
class DisciplinaDetailView(APIView):
    # puxa uma disciplina e seus atributos pela pk
    def get (self, request,pk):
        try:
            # se achar retorna a disciplina e dados
            disciplina = DisciplinaModel.objects.get(pk=pk)
            serializer= DisciplinaSerializer(disciplina)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # se não achar, aparece ums mensagem de erro
        except DisciplinaModel.DoesNotExist:         
            return Response("disciplina não encontrada", status=status.HTTP_404_NOT_FOUND)
        # tratamento de excessão com erro 400
        except Exception as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        
    # atualizar/ modificar disciplina
    def put(self, request, pk):
        try:
            disciplina=DisciplinaModel.objects.get(pk=pk) 
            #é possível alterar apenas alguns campos do objeto, não necessariamente todos
            serializer = DisciplinaSerializer(disciplina, data= request.data, partial=True)
            if(serializer.is_valid()):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # tratamento de erro 400 
        except Exception as error:
             return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
    
    # deletar disciplina 
    def delete(self, request, pk):
        try:
            disciplina = DisciplinaModel.objects.get(pk=pk)
            disciplina.delete()
            return Response( "disciplina deletada com sucesso!",status= status.HTTP_204_NO_CONTENT)
        except DisciplinaModel.DoesNotExist:
                return Response("disciplina não encontrada", status=status.HTTP_404_NOT_FOUND)