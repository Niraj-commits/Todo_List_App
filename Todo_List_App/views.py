from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(response):
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
    return render(response,'home_page.html',context)

def about(response):
    context = {"name":"This app was made by niraj"}
    return render(response,'about.html',context)

def contact(response):
    contacts = [
        {"name":"Ram","Phone":9808978900},
        {"name":"Shyam","Phone":89898989},
        {"name": "Alice", "number": 12345},
        {"name": "Bob", "number": 67890},
        {"name": "Charlie", "number": 54321},
        {"name": "Diana", "number": 98765}
    ]
    context = {"name":"contact page","contact":contacts}
    return render(response,'contact.html',context)

def index(response):
    context = {"name":"index page"}
    return render(response,'index.html',context)
    