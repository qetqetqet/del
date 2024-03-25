from django.shortcuts import render
from .models import Todo  # Import your Todo model

def index(request):
    todos = Todo.objects.all()  # Get all todo items
    return render(request, 'todos/index.html', {'todos': todos})
