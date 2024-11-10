from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('honey_list')
        else:
            return redirect('register')
    elif request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('honey_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('honey_list')
    elif request.method == 'GET':
        form = AuthenticationForm(request)

    return render(request,'login.html',context={'form': form},)

def logout_view(request):
    logout(request)
    return redirect('honey_list')