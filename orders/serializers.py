from rest_framework import serializers
from .models import Order, OrderItem
from home.models import Product
from account.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product_name", "product_price", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["order_id", "customer", "items", "total_price", "created_at"]
