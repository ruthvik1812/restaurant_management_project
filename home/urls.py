from django.urls import path
from . import views.

urlpatterns = [
    path('',views.home,name ="home"),
    path("contact/",views.contact,name="contact"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("feedback/",views.submit_feedback, name="home"),
    path("staff/login/",staff_login, name="home"),
    path("reservation/",view.reservations ,name="home"),
    path("menu/",views.menu_list, name="home"),
    path("add-to-cart/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("faq/",views.faq_view, name="home"),
    path('order/', views.order_page,name='home'),
    path('login/', views.logout_view, name='login'),
    path('logout/'),views.logout_view, name='logout'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path("about/", views.about, name="about"),
    path('chefs/', views.chefs, name='chefs'),
    path('reservations/', views.reservations, name='reservation'),
    path('categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    path('api/',include('home.urls')),
    ]

if settings.DEBUG:
    urlpatterns += Static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)