from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib.auth.models import auth, User #use for login, logout
from django.contrib import messages
from .models import List
from os import name

# Create your views here.
def index(request):
    #create list from models and after that push it to templates index.html
    lists = List.objects.all()
    return render(request, "index.html", {'lists': lists})


def  register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already In Used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already In User')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else: 
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) 
            return redirect('/')
        else:
            messages.info(request, 'Credential is invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def post(request, sth):
    
    return render(request, 'post.html', {'sth':sth})

def count(request):
    # word = request.POST['text']
    posts = [1,2,3,4, 'john', 'na']
    # count = len(word.split())
    return render(request, 'count.html',{'posts': posts})