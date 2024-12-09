
from django.shortcuts import render, redirect
from .models import Task

# View to list tasks
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('list_tasks')
    return render(request, 'add_task.html')
