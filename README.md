# Gerenciador de Estudos: API de Gestão de Alunos, Disciplinas e Tarefas

### O que é o projeto:
esse projeto é uma API em Django para ajudar alunos a gerenciarem suas disciplinas e
tarefas. Ela contêm todas as solicitações HTTP: GET, POST, PUT e DELETE, ou seja, é possível listar, adicionar, atualizar e deletar alunos, disciplinas e tarefas. 

### Requisitos:
-  Python 3.x
- Django 3.x
- Django REST Framework 

### Instalação

Clone esse repositório:

```bash
  https://github.com/camiyuka/api_students.git
``` 
Crie um ambiente virtual: 
```bash
  Python -m venv .env
``` 
Ative o ambiente virtual:
```bash
\.env\Scripts\activate
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
Prepare o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### Explicação dos Endpoints:
GET e POST alunos:
```bash
    api/alunos/ 
  ```
PUT, GET e DELETE alunos:
```bash
    api/alunos/<pk>/
  ```
GET E POST disciplina:
```bash  
    api/disciplina/
  ```
PUT, GET e DELETE disciplina:

```bash
    api/disciplina/<pk>/
  ```
GET e POST tarefas:
```bash
    api/tarefa/'
  ```
PUT, GET e DELETE tarefas:
```bash
    api/tarefa/<pk>/
  ```
GET aluno
```bash
      api/alunos/<aluno>/tarefas/'
  ```
