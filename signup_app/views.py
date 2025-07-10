from django.shortcuts import render, redirect
from .models import User_signup  # Your custom model
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User_signup.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        user = User_signup(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Account created successfully!')
        return redirect('login')  
    
    return render(request, 'signup_app/signup.html')


