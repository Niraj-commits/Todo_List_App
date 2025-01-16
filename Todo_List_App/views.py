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