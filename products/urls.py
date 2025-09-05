from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', views.menu_list, name='home'),
    path(''),views.home, name='home'),
]