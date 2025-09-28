from django.urls import path
from .views import *

urlpatterns = [
    path('menu/',,views.menu_list,name='menu_list'),
    path("history/", OrderHistoryView.as_view(), name="order-history"),
    path('orders/<str:order_id/', OrderDetailView.as_view(), name='order-detail'),
]