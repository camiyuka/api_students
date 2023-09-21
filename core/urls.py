from api.views.alunoView import AlunoView
from api.views.alunoDetailView import AlunoDetailView

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', AlunoView.as_view()),
    path('alunos/<int:pk>/', AlunoDetailView.as_view())
]
