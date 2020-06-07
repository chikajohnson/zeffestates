from django.shortcuts import render, redirect

def login(request):
    return render(request, 'accounts/login.html', context={})

def register(request):
    return render(request, 'accounts/register.html', context={})

def logout(request):
    return redirect('index')


def dashbaord(request):
    return render(request, 'accounts/dashboard.html', context={})