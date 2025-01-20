
from django.urls import path
from .views import *

urlpatterns = [
    path('task/',task),
    path('task/create/',create_tasks),
]