from django.contrib import admin
from .models import todo_list


@admin.register(todo_list)


# Register your models here.
class Todo_List_Admin(admin.ModelAdmin):
    list_display = ["Name","Description",'Status']
    list_filter = ['Status']
    list_per_page = 10
    list_editable = ['Status']
    search_fields = ['Name']