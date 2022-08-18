from ast import Pass
from unittest import result
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def main(request):
    
    return render (request, 'main.html')



def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['id']
        paswd = request.POST['pass']
        user = auth.authenticate(username=uname,password=paswd)
        if user is not None :
            auth.login(request, user)
            messages.info(request, 'Login Successfull')
            return render(request, 'main.html',{ 'result' : uname})
        else :
            messages.info(request, 'Invalid Credentials')
            return render(request , 'home.html')   
    else :
         return render(request, 'main.html')


def exit(request):
    
    return render (request, 'home.html')