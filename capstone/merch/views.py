from django.shortcuts import render

# Create your views here.
def clothes(request):
    """When called by urls.py, this function will open the merchandise page
    called merch.html"""
    return render(request,"merch.html")