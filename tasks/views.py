from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm
                                                })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'Username already exists'
                                                        })
        return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'Password do not match'
                                                        })


def tasks(request):
    return render(request, 'tasks.html')

def signout(request):
    "signout instead logout to avoid reserved word"
    logout(request)
    return redirect('home')


def signin(request):
    "signin instead login to avoid reserved word"
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
            })
    else:
        #if method == 'POST'
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:    
            #if user is not valid and show with an error
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            })
        else:
            #if user exist
            login(request, user)    #save session of user
            return redirect('tasks')