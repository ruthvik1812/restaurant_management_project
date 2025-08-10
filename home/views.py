from django.shortcuts import render

# Create your views here.
from djang.shortcuts import render

def homepage(request):
    return render (request,'homepage.html')