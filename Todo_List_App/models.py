from django.db import models

# Create your models here.

class todo_list(models.Model):
    Name = models.CharField( max_length=50)
    Description = models.TextField()
    Status = models.BooleanField(default=True)
    Completion_Time = models.DateTimeField(blank=False,null=True)
    Start_Time = models.DateTimeField(auto_now_add = True)

