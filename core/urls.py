from api.views.alunoView import AlunoView


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', AlunoView.as_view())
]
