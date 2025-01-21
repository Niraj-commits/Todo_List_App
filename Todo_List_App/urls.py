
from django.urls import path
from .views import *

urlpatterns = [
    path('task/',task),
    path('task/create/',create_tasks),
    path('task/<pk>/',change_status),
    path('task/<pk>/edit/',edit_task),
    path('task/<pk>/delete/',delete_task),
]   