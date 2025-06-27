from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

def login(request):
    return render (request, 'login_app/login.html', context = {})

def userAuthenticaton(request):
    if request.method == "POST":
        
        userUsername = request.POST.get("username")
        userPassword = request.POST.get("pass")
        
        try:
            user = User.objects.get(username = userUsername, password = userPassword)
            request.session ['userId'] = user.id
            return redirect ('blog')
        
        except User.DoesNotExist:
            error = "Invalid username or password"
            messages.error (request, error)
            return redirect ('login')
    else:
        return redirect ('login')
        
    