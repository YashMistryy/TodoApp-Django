from django import forms
from .models import TodoTask
class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = '__all__'