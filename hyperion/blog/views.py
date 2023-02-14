from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
     """When called by urls.py, this function will open the blog page
    called index.html"""
    return render(request,"index.html")