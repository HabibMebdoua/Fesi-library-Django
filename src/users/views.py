from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User

def base(request):
    users = User.objects.count()
    context = {
        'users':users,
    }
    return render(request , '_partials/navbar.html',context)

def register(request):
    form = UserCreationForm()
    users_count = User.objects.count()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if users_count < 1 : 
            if form.is_valid():
                user = form.save()
                login(request , user)
                messages.info(request , 'User has been registered')
                return redirect('index')
            print('='*100)
            print(users_count)
        else:
            messages.warning(request , 'You are not allowed to create an account')
            print(users_count)
    context = {
        'form':form,
    }
    return render(request , 'users/register.html',context)
