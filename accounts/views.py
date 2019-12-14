from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


# Create your views here.
def index(request):
    """create view for index.html"""
    return render(request, 'index.html')


def logout(request):
    """logout users"""
    auth.logout(request)
    messages.success(request, "You have successfully been loged out!")
    return redirect(reverse('index'))


def login(request):
    """return a login page"""
    return render(request, 'login.html')
