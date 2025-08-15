from django.urls import path
from . import views.

urlpatterns = [
    path('',views.home,name ='home'),
    path('contact/',views.contact,name='con(tact'),
    path('staff/login/',staff_login, name='staff-login'),
    
]