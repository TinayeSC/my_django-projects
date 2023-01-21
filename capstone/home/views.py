from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"bandpage.html")

def entrance(request):
    return render(request,"home_vid.html")