from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm



def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        messages.success(request, 'You must be logged in to view that page.')
        redirect('signup')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
        else:
            form = NewUserForm()
            return render(request, 'signup.html', {'form':form})
    return render(request, 'signup.html', {'form':form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, 'signin.html', {'form':form})
    return render(request, 'signin.html', {'form':form})


def signout(request):
    logout(request)
    
    return redirect('signup')

