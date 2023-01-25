from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
# Create your views here.

def index(req):
    todos = Todo.objects.filter(title__contains=req.GET.get('search',''))
    context = {'todos':todos}
    return render(req, 'todo/index.html',context)

def view(req, id):
    todo = Todo.objects.get(id=id)
    context = {'todo':todo}
    return render(req, 'todo/view.html',context)

def edit(req, id):
    todo = Todo.objects.get(id=id)
    if req.method == 'GET':
        form = TodoForm(instance=todo)
        context = {'form':form, 'id':id}
        return render(req, 'todo/edit.html',context)
    if req.method == 'POST':
        form = TodoForm(req.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(req,message='Tarea actualizada.', extra_tags='alert-success')
        context = {'form':form, 'id':id}
        return render(req, 'todo/edit.html',context)



def create(req):
    if(req.method == 'GET'):
        form = TodoForm()
        context = {'form': form}
        return render(req, 'todo/create.html',context)
    if req.method == 'POST':
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')

def delete(req, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')