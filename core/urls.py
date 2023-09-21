from api.views.alunoView import AlunoView
from api.views.alunoDetailView import AlunoDetailView
from api.views.disciplinaView import DisciplinaView
from api.views.disciplinaDetailView import DisciplinaDetailView
from api.views.tarefaView import TarefaView
from api.views.tarefaDetailView import TarefaDetailView

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/', AlunoView.as_view()),
    path('api/alunos/<pk>/', AlunoDetailView.as_view()),  
    path('api/disciplina/', DisciplinaView.as_view()),
    path('api/disciplina/<pk>/', DisciplinaDetailView.as_view()),
    path('api/tarefa/', TarefaView.as_view()),
    path('api/tarefa/<pk>/', TarefaDetailView.as_view())
]
