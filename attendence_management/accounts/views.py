from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import time


# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
        else:
            messages.info(request, 'Password did not match')
            print('password not correct')

        messages.info(request, 'User Created Successfully')
        print('user created')
        time.sleep(3)
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':  # checking if method is post
        username = request.POST['username']  # fetching the username from page
        password = request.POST['password']  # fetching the password from page
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # above condition is always false
            auth.login(request, user)
            print('login successful')
            return redirect('home.html')
        else:
            messages.info(request, 'Username or Password Not correct')
            print('login unsuccessful')
            return redirect('home')  # problem here so look it not auth user
    else:
        return render(request, 'indexo.html')
