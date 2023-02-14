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
    """This function takes the user to the login page
    
        """
    return render(request, 'authentication/login.html')


def user_logout(request):
    """This function logs the user out and returns them to the login page
    
        """
    logout(request)
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    """This function defines how to authenticate a user. It takes the user 
        input and tries to log them in. 
        
        :param str username: This requests the user to type the username
        :param str password: This requests the user to type their corresponding
            password
        :param user: This authenticates the information entered by the user. If it 
            matches a user that has been saved in the database, then a welcome page is
            displayed by calling the show user function. If it does not match to an existing
            user, then the output will be None, and the user is redirected to the login page where
            they can select to register. 
            
            """
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
    """ This function displays a welcome page upos succesfull user login.
    
        """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def registration_page(request):
    """ This function registers new users by requesting the necessarry information.
        
        """
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form':form}
    return render(request,"authentication/register.html",context)