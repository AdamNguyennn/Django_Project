from django.shortcuts import render
from django.http import HttpResponse
from os import name

# Create your views here.
def index(request):
	name = "Nam Anh"
	return render(request, "index.html", {'name': name})

def count(request):
    word = request.POST['text']
    count = len(word.split())
    return render(request, 'count.html',{'count':count})