from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","name","email","phone_number")
    search_fields = ("name","email","phone_number")

@admin.register(RestaurantLocation)
class RestaurantLocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address","city","state", "zip_code", "phone")
    search_fields = ("name", "city", "state", "phone")
    