from django.contrib import admin
from .models import Restaurant, MenuItem, Contact, RestaurantLocation, Feedback
# Register your models here.

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','owner_name', 'email', 'phone_number', 'city')
    search_fields = ('name', 'owner_name', 'city')
    list_filter =('city',)
    ordering = ('-created_at')
#------- RESTAURANT INFO ------------#
@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')
#---------MENU ITEM ADMIN ----------#
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price','restaurant')
    search_fields = ('name','descrption')
    list_filter = ('restaurant',)
    ordering =('name',)
# ------ Contact Admin ------------ #
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
# ------------- RESTAURANT LOCATION ADMIN --------------#
@admin.register(RestaurantLocation)
class RestaurantLocation(admin.ModelAdmin):
    list_display = ('name', 'comment', 'submitted_at')
    search_fields = ('name', 'comment')
    list_filter =('city', 'state')
#--------------------- FEEDBACK ADMIN ----------------#
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','comment', 'submitted_at')
    search_fields = ('name', 'comment')
    ordering = ('-submitted_at',)