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
        return redirect('/')
    return render(request,'create.html')

def change_status(request,pk):
    task = todo_list.objects.get(pk = pk)
    task.Status = True
    task.save()
    return redirect('/')

def edit_task(request,pk):
    task = todo_list.objects.get(pk = pk)
    context = {"tasks":task}
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
    return render(request,'edit.html',context)
        
def delete_task(request,pk):
    task = todo_list.objects.get(pk = pk)
    context = {"tasks":task}
    task.delete()
    return redirect('/')
