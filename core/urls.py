from api.views.alunoView import AlunoView
from api.views.alunoDetailView import AlunoDetailView
from api.views.disciplinaView import DisciplinaView
from api.views.disciplinaDetailView import DisciplinaDetailView

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', AlunoView.as_view()),
    path('alunos/<pk>/', AlunoDetailView.as_view()),  
    path('disciplina/', DisciplinaView.as_view()),
    path('disciplina/<pk>/', DisciplinaDetailView.as_view())
]
