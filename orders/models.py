from django.db import models
from django.contrib.auth.models import User
from products.models import product

# ---- ORDER STSTUS ------ #
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
# -------------- ORDER ---------- #
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey (
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} ({self.status})"


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
        order = models.ForeignKey(order,on_delete=models.CASCADE,related_name="items")
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
            return f"{self.quantity)} * {self.product.name} (Order {self.order.id})"