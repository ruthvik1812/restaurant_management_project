from django.shortcuts import render
from django.conf import settings
# Create your views here.


def home(request):
    restaurant = RestaurantInfo.objects.first()
    return render(request,'home.html',{'phone_number' :phone_number})
   