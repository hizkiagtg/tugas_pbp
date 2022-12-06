from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
        data = Task.objects.filter(user = request.user)
        context = {
            'list_task': data,
            'nama': request.user,
        }
        return render(request, "todolist.html", context)
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")        
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todolist/')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def add_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = datetime.now()
        description = request.POST.get('description')
        newTask = Task(
            user = request.user,
            date = date,
            title = title,
            description = description,
        )
        newTask.save()
        return HttpResponse(serializers.serialize("json",[newTask]), content_type="application/json")
    return HttpResponseNotFound()
    
def deleted_ajax(request, id):
    if(request.method == 'GET'):
        Task.objects.get(pk=id).delete()
    return HttpResponse('')

def deleted(request, id):
    Task.objects.get(pk = id).delete()
    return redirect("todolist:show_todolist")

def finished(request, id):
    task = Task.objects.get(pk = id)
    task.is_finished = True
    task.save()
    return redirect("todolist:show_todolist")
