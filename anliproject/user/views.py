from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone

def register(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['re-password']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password'],
                date_joined = timezone.now()
            )
        auth.login(request, user)
        return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    print("logout complete")
    return redirect('/')