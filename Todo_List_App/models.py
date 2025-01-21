from django.db import models

# Create your models here.

class todo_list(models.Model):
    Name = models.CharField( max_length=50)
    Description = models.TextField()
    Status = models.BooleanField(default=False)
    Start_Time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Name
