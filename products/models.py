from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    created_at =
    def __str__(self):
        return str(self.item_name)

class Order(models..Model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyTOManyField(Menu)

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"