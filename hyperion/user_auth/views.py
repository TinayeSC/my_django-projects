from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
            )   
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))
    
    
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def registration_page(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form':form}
    return render(request,"authentication/register.html",context)