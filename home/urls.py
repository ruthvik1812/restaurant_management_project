from django.urls import path
from . import views.

urlpatterns = [
    path('',views.home,name ="home"),
    path("contact/",views.contact,name="home"),
    path("feedback/",views.submit_feedback, name="home"),
    path("staff/login/",staff_login, name="home"),
    path("reservation/",view.reservations ,name="home"),
    path("menu/",views.menu_list, name="home"),
    path("add-to-cart/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("faq/",views.faq_view, name="home"),
    path('order/', views.order_page,name='order')
]

if settings.DEBUG:
    urlpatterns += Static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)