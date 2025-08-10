from django.shortcuts import render
from homepage(re)
# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request , 'home/index.html')