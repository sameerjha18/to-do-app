from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):

    tasks = Task.objects.all()
    form = taskForm()

    if request.method =='POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'task/list.html', context)

def updateTask(request, pk):
    tasks = Task.objects.get(id=pk)

    form = taskForm(instance=tasks)

    if request.method == "POST":
        form = taskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'task/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'task/delete.html', context)