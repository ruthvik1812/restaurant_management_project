from django.contrib import admin
from .models import Menu, order


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name', 'price')
    search_fields =('name',)
    list_filter = ('price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name','created_at')
    search_fields = ('customer_name',)
    filter_horizontal = ('items',)
