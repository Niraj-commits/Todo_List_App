from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(response):
    person = [
        {
            "name": "Ram",
            "age":23,
        },
        {
            "name": "Sita",
            "age":23,
        },
        {
            "name": "GIta",
            "age":23,
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
    context = {"name":"contact page"}
    return render(response,'contact.html',context)

def index(response):
    context = {"name":"index page"}
    return render(response,'index.html',context)
    