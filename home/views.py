from django.shortcuts import render
from django.conf import settings
# Create your views here.


def home(request):
    restaurant_name = getattr(settings,'RESTAURANT_NAME','My Restaurant')
    return render(request,'home.html', {'restaurant_name':restaurant_name}{'phone_number' :phone_number})
   