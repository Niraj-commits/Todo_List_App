from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def task(request):
    
    task = todo_list.objects.all()
    context = {"tasks":task}
    return render(request,'task.html',context)

def create_tasks(request):
    
    if request.method == "POST":
        name = request.POST.get('name') #returns data in dictionary as payload
        description = request.POST.get('description')
        todo_list.objects.create(Name= name,Description = description)
        return redirect('task/')
        
    
    return render(request,'create_task.html')

def change_status(request,pk):
    task = todo_list.objects.get(pk == pk)
    task.status = True
    task.save()
    return redirect('task.html')
    