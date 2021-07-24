from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from os import name

# Create your views here.
def index(request):
    #create list from models and after that push it to templates index.html
    lists = List.objects.all()
    return render(request, "index.html", {'lists': lists})

def count(request):
    word = request.POST['text']
    count = len(word.split())
    return render(request, 'count.html',{'count':count})