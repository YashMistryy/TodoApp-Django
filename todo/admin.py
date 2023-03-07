from django.contrib import admin

from .models import TodoTask

class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ('taskName','isCompleted', 'dateOfCreation')
    
# Register your models here.
admin.site.register(TodoTask,TodoTaskAdmin)
