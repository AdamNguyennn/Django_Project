from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from os import name

# Create your views here.
def index(request):
    #create list from models and after that push it to templates index.html
    list1 = List()
    list1.id = 1
    list1.name = "study"
    list1.description = "learning docker, django, devNet"
    list1.is_true = True

    list2 = List()
    list2.id = 2
    list2.name = "cleaning"
    list2.description = "living room, kitchen, my room "
    list2.is_true = True

    list3 = List()
    list3.id = 3
    list3.name = "do exercise"
    list3.description = "push up, pull up, abs,..."
    list3.is_true = False
    
    list4 = List()
    list4.id = 4
    list4.name = "playing"
    list4.description = "Lol, cs:go, ...."
    list4.is_true = True
    
    lists = [list1, list2, list3, list4]

    return render(request, "index.html", {'lists': lists})

def count(request):
    word = request.POST['text']
    count = len(word.split())
    return render(request, 'count.html',{'count':count})