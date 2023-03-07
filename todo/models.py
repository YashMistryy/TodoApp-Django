from django.db import models

class TodoTask(models.Model):
     taskName = models.CharField(max_length=100)
     dateOfCreation = models.DateTimeField(auto_now_add=True)
     isCompleted = models.BooleanField(default=False)
     
     def __str__(self):
          return self.taskName