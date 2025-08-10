from django.urls import path
from .views import *

urlpatterns = [
    path('about/',views.homepage,name='homepage'),
    
]