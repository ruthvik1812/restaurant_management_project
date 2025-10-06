from django.db import models
from django.contrib.auth.models import User
from products.models import product
from account.models import User
from home.models import product

class ActiveOrderManager(models.manager):
    def get_active_orders(self):
        """
        Returns only orders with 'PENDING' or 'PROCESSING'.
        """
        return self.filter(status__in=['PENDING', 'PROCESSING'])

class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING","Pending"),
        ("CONFIRMED","Confirmed"),
        ("PREPARING","preparing"),
        ("DELIVERED","Delivered"),
        ("CANCELLED","Cancelled"),
    ]

    order_id = models.CharField(max_length=50,unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_items = models.ManyToManyField(product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = models.manager()
    active_orders = ActiveOrderManager()
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order{self.id} by {self.customer.username}"

    def calculate_total(self):
        """
        Calculate total cost of all items in this order.
        """
        total =sum(item.product.price * item.quantity for item in self.items.all())
        self.total_amount = total
        self.save()
        return total

    class OrderItem(models.Model):
        order = models.ForeignKey(Order,, on_delete=models.CASCADE,related_name="items")
        product = models.ForeignKey(product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return f"{self.quantity)} * {self.product.name} (Order {self.order.id})"