from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail

def registerview(request):
    fm = RegisterForm()
    context = {
        'registerform': fm
    }
    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()
            username = user.cleaned_data.get('username')
            email = user.cleaned_data.get('email')
            send_mail(
                'Registration Successful',
                f'{username}, you have successfully registered.',
                "sonali09245@gmail.com",  
                [email],  
                fail_silently=False,
            )
            messages.success(request, 'User Created Successfully. You can now log in.')
            return redirect('login')  
    return render(request, 'accounts/register.html', context)

def loginview(request):
    context = {
        'loginform': LoginForm()
    }
    if request.method == 'POST':
        fm = LoginForm(data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            password = fm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_authenticated:
                    login(request, user)
                    messages.success(request, f'Login Successful {username}')
                    return redirect('filtered_movies')  
    return render(request, 'accounts/login.html', context)


def logoutview(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')  

@login_required(login_url='login')
def home(request):
    return redirect('filtered_movies') 

