from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo


def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'todos/todo_list.html',context)


def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')