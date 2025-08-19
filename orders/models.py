from django.db import models
from django.contrib.auth.models import User
from products.models import products

class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING","Pending"),
        ("CONFIRMED","Confirmed"),
        ("PREPARING","preparing"),
        ("DELIVERED","Deliverd"),
        ("CANCELLED","Cancelled"),
    ]

    customer =models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order{self.id} by {self.customer.username}"

    def calculate_total(self):
        total =sum(item.product.price * item.quantity for item in self.items.all())
        self.total_amount = total
        self.save()
        return total

    class OrderItem(models.Model):
        order = models.ForeignKey(Order,, on_delete=models.CASCADE,related_name="items")
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(Self):
            return f"{self.quantity)} * {self.product.name} (Order {self.order.id})"