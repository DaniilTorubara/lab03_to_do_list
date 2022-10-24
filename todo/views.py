import re
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from todo.models import TODO
from .forms import ToDoForm

# Create your views here.

def createtodos(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodos.html', {'form':ToDoForm()})
    else:
        try:
            form = ToDoForm(request.POST)
            newtodo = form.save(commit = False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodos.html', {'form':ToDoForm()})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error': 'Вы ввели ошибочные данные, попробуйте еще раз'})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error': 'Неверные имя пользователя или пароль'})
        else:
            login(request, user)
            return redirect('currenttodos')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def home(request):
    return render(request, 'todo/home.html')

def currenttodos(request):
    todo_tasks = TODO.objects.filter(user = request.user, completion_date__isnull = True)
    return render(request, 'todo/currenttodos.html', {'tasks': todo_tasks})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Данный пользователь уже зарегистрирован'})
 
        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают'})
