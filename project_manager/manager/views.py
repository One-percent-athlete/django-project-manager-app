from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView


from .models import Project, Task
from .forms import TaskForm


def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()

    context = {'projects':projects}
    return render(request, 'projects.html', context)


def project_details(request, pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {'project':project,'project_tasks': project_tasks}
   return render(request, 'project-details.html', context)

def tasks(request):
    user_tasks =Task.objects.filter(assignee=request.user)
    tasks = Task.objects.filter(assignee=None)
 
    context = {'tasks':tasks,'user_tasks':user_tasks}
    return render(request, 'tasks.html',context)

def task_details(request,pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task':task}
    return render(request, 'task-details.html',context)


def create_task(request):
    if request.method == "POST":
       form =TaskForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('tasks')
    else:
        form = TaskForm
        return render(request, 'create-task.html', {'form': form})
    
def joinTask(request,pk):
   task =Task.objects.get(id=pk)
   task.assignee=request.user
   task.save()
   return redirect('tasks')
    


class TaskListView(ListView):
   model = Task
   template_name = 'tasks.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ["name","description"]
    template_name = 'create-project.html'
    success_url = reverse_lazy('projects')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update-task.html'
    fields = ["title","description","project","assignee","due_date","status"]
    success_url = reverse_lazy('tasks')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'update-project.html'
    fields = ["name","description"]
    success_url = reverse_lazy('projects')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete-task.html'
    success_url = reverse_lazy('tasks')
 
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'delete-project.html'
    success_url = reverse_lazy('projects')



