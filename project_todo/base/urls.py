from .import views
from django.contrib import admin
from django.urls import path, include
from .views import Tasklist, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
path('register/',RegisterPage.as_view(),name='register'),
    path('tasklist/',Tasklist.as_view(),name="task"),
    path('taskdetail/<int:pk>/',TaskDetail.as_view(),name="taskdetail"),
    path('taskcreate/', TaskCreate.as_view(), name="taskcreate"),
    path('taskupdate/<int:pk>/', TaskUpdate.as_view(), name="taskupdate"),
    path('taskdelete/<int:pk>/',TaskDelete.as_view(),name='taskdelete')
]
