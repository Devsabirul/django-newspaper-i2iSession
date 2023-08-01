from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'login/signin.html')
    else:
        return redirect('/')


def logout_(request):
    logout(request)
    return redirect('/')


def signup(request):
    if not request.user.is_authenticated:
        username_msg = ""
        email_msg = ""
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            avatar = request.FILES['avatar']
            number = request.POST['number']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            user_valid_check = User.objects.filter(username=username).exists()
            email_valid_check = User.objects.filter(email=email).exists()
            if user_valid_check:
                username_msg = "User name already exist, please choose new one."
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                profile = Profile.objects.create(
                    user=user, avatar=avatar, number=number)
                if profile:
                    return redirect('/')
        return render(request, 'login/signup.html', {'umsg': username_msg, 'email_msg': email_msg})
    else:
        return redirect('/')
