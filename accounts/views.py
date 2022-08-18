from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST' :
        uname=request.POST['uname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 == pass2 :
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username Taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                print('Email Taken')
                return redirect('register')
            else :
                user = User.objects.create_user(username=uname, password=pass1, email=email)
                user.save();
                messages.info(request, 'created user')
                return redirect('login')
        else:
            messages.info(request, 'Password MissMatch')
            return redirect('register')
        
        
    else:
        return render(request, 'register.html')