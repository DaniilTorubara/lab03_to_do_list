"""lab03_to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name = 'signupuser'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
    path('login/', views.loginuser, name = 'loginuser'),
    path('current/', views.currenttodos, name = 'currenttodos'),
    path('completed/', views.completedtodos, name = 'completedtodos'),
    path('create/', views.createtodos, name = 'createtodos'),
    path('task/<int:task_pk>', views.viewtask, name = 'viewtask'),
    path('task/<int:task_pk>/complete', views.completedtask, name = 'completedtask'),
    path('task/<int:task_pk>/delete', views.deletedtask, name = 'deletedtask'),


]
