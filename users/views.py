from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})