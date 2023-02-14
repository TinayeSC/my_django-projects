from django.shortcuts import render

# Create your views here.


def index(request):
     """When called by urls.py, this function will open the album page
    called singles.html"""
    return render(request,"singles.html")