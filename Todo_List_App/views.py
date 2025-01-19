from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home_page(request):
    person = [
        {
            "name": "Ram",
            "age":43,
        },
        {
            "name": "Sita",
            "age":63,
        },
        {
            "name": "GIta",
            "age":8,
        },
        {
            "name": "Rita",
            "age":23,
        },
        ]
    context = {"name":"Home Page","persons":person}
    return render(request,'home_page.html',context)

def about(request):
    context = {"name":"This app was made by niraj"}
    return render(request,'about.html',context)

def contact(request):
    contacts = [
        {"name":"Ram","Phone":9808978900},
        {"name":"Shyam","Phone":89898989},
        {"name": "Alice", "Phone": 12345},
        {"name": "Bob", "Phone": 67890},
        {"name": "Charlie", "Phone": 54321},
        {"name": "Diana", "Phone": 98765}
    ]
    context = {"name":"Contact Page","contact":contacts}
    return render(request,'contact.html',context)

def index(request):
    context = {"name":"index page"}
    return render(request,'index.html',context)
    

def task(request):
    
    task = todo_list.objects.all()
    context = {"tasks":task}
    return render(request,'task.html',context)