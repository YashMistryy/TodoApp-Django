from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import TodoTask
from .forms import TaskForm

def showTodos(request):
    if(request.method == 'POST'):
        tasklistx = TodoTask.objects.all().order_by('-dateOfCreation')[:5]
        taskformx = TaskForm()
        
        if(tasklistx.count() >= 5 ):
            return render(request,'index.html',{'tasklist':tasklistx,'taskform':taskformx,'maxError':'you have reached maximum allwed tasks for the day!\n try completing the pending tasks first'})
          
        task = request.POST.get("taskName")
        dateOfCreation = request.POST.get("dateOfCreation")
        isCompleted = True if request.POST.get("isCompleted") == "on" else False
        taskx = TodoTask(taskName = task,dateOfCreation =  dateOfCreation,isCompleted = isCompleted )
        taskx.save()
        return redirect('/')
    tasklisty = TodoTask.objects.all().order_by('-dateOfCreation')[:5]
    taskformy = TaskForm()
    if(TodoTask.objects.count() == 0):
      return render(request,'index.html',{'taskform':taskformy,'error':'enter something to make a task!'})
    return render(request,'index.html',{'tasklist':tasklisty,'taskform':taskformy})
  
def updateTask(request,id):
  task = TodoTask.objects.get(id = id) 
  taskForm = TaskForm(instance=task)
  
  if request.method == 'POST':
    taskForm = TaskForm(request.POST,instance=task)
    if taskForm.is_valid():
      taskForm.save()
      return redirect('/')
  return render(request,'update-task.html',{'form':taskForm})
     
def deleteTask(request,id):
  task = TodoTask.objects.get(id = id) 
  taskForm = TaskForm(instance=task)
  if(request.method == 'POST'):
    task.delete()
    return redirect('/')
  return render(request,'delete-task.html',{'task':task})  