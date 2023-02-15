from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): 
    """This function, when called by urls.py, will open the homepage of the band website
        called bandpage.html
        """
    return render(request,"bandpage.html")
   
   

def entrance(request):
    """This function, when called by urls.py, will open the cover page of the band website
       called home_vid.html
       """
    return render(request,"home_vid.html")
    
    