from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login
from django.contrib import messages

from .models import CustomUser

# Create your views here.

# Sign Up 
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Check if user with the username or email already exists
        if CustomUser.objects.filter(username = username).exists(): 
            messages.error(request, f'User with this username {username} already exists!', extra_tags='username')
            return redirect('users:signup_user')
        
        elif(CustomUser.objects.filter(email = email).exists()):
            messages.error(request, f'User with this email already exists!', extra_tags='email')
            return redirect('users:signup_user')

        # Create the user
        new_user = CustomUser.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = make_password(password)
        )
        auth_login(request, new_user)
        return redirect('posts:home')
    
    return render(request, 'users/signup.html')


# Log in
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser.objects.filter(email = email).first()

        if (user):
            if (check_password(password, user.password)):
                auth_login(request, user)
                return redirect('posts:home')
            else:
                messages.error(request, f'Wrong password! Please try again', extra_tags='password')
                return redirect('users:login_user')
        else:
            messages.error(request, 'No users with this email found!', extra_tags='email')
            return redirect('users:login_user')
        
    return render(request, 'users/login.html')