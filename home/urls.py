from django.urls import path
from . import views.

urlpatterns = [
    path('',views.home,name ="home"),
    path("contact/",views.contact,name="contact"),
    path("feedback/",views.submit_feedback, name="feedback"),
    path("staff/login/",staff_login, name="staff-login"),
    path("reservation/",view.reservations ,name="reservation"),
    path("menu/",views.menu_list, name="menu"),
]