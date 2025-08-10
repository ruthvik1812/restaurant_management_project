from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request , 'home/index.html')