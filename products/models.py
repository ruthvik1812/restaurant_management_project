from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
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

class TodaysSpecial(models.Model):
    name = models.CharField(max_length=200, verbose_name="Special Item Name")
    description = models.TextField(verbose_name="Special Item Description", blank=True, null=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="price")
    image =  models.ImageField(upload_to="specials/", blank=True, verbose_name="Special Dish Image")
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = "Today's special"
    verbose_name_pural ="Today's Specials"
    ordering = [-'created_at']
def __str__(self):
    return self.name