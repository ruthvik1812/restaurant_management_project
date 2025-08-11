from django.shortcuts import render

# Create your views here.
from djang.shortcuts import render

def home(request):
    return HttpResponse("home.html")
   