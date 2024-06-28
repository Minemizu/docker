from django.urls import path
from mytodo import views as mytodo
from unicodedata import name
from .import views


urlpatterns = [
    path("", mytodo.index, name="index"),
    path("add/", mytodo.add, name="add"),
    path("update_task_complete/", mytodo.Update_task_complete, name="update_task_complete"),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'), 
    path('/<str:pk>/update', mytodo.update_view, name='update')
]
