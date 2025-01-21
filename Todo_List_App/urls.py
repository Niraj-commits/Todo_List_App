
from django.urls import path
from .views import *

urlpatterns = [
    path('',task),
    path('create/',create_tasks),
    path('<pk>/',change_status),
    path('<pk>/edit/',edit_task),
    path('<pk>/delete/',delete_task),
]   