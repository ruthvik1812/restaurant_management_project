from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class OrderItemline(admin.TabularInline):
    model = OrderItem
    extra = 1
@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display =("id","customer","status","total_amount","created_at")
    list_filter = ("status","created_at")
    search_fields = ("customer__username","customer__email")
    inlines = [OrderItemline]

admin.site.register(OrderItem)