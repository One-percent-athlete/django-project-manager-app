from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('project_details/<int:pk>', views.project_details, name='project-details'),
    path('tasks', views.tasks, name='tasks'),
    path('task_details/<int:pk>', views.task_details, name='task-details'),
    path('join-task/<int:pk>', views.joinTask, name ='join-task'),
    path('create_task', views.create_task, name ='create-task'),
    path('create_project', views.ProjectCreateView.as_view(), name ='create-project'),
    path('update_task/<int:pk>', views.TaskUpdateView.as_view(), name ='update-task'),
    path('update_project/<int:pk>', views.ProjectUpdateView.as_view(), name ='update-project'),
    path('delete_task/<int:pk>', views.TaskDeleteView.as_view(), name ='delete-task'), 
    path('delete_project/<int:pk>', views.ProjectDeleteView.as_view(), name ='delete-project'),
]