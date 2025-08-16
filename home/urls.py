from django.urls import path
from . import views.

urlpatterns = [
    path('',views.home,name ='home'),
    path("contact/",views.contact,name="contact"),
    path("staff/login/",staff_login, name="staff-login"),
    path("reservation/",view.reservations ,name="reservation"),
    
]