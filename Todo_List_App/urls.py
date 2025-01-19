
from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page),
    path('about/',about),
    path('contact/',contact),
    path('task/',task),
]