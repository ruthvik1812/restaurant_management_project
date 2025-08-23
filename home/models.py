from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="RR Restaurant"
    )
    
    owner_name = models.CharField(
        max_length=255,
        verbose_name="Ruthvik Raj Chintala"
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name="ruthvikraj.chintala1812@gmail.com"
    )
    
    phone_number = models.CharField(
        max_length=15,
        verbose_name="8639139326"
    )
    
    address = models.TextField(
        verbose_name=" # 17-3,Ambedkar street, huzurabad,karimnagar district"
    )
    
    city = models.CharField(
        max_length=100,
        verbose_name="karimnagar"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Registered On"
    )



    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.city}"

# Menu Model
class Menu(models.Model):
    restaurant = models.foreignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu-item",
        verbose_name="Restaurant"
    )   
    name = models.CharField(max_length=100, verbose_name="dish Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description)")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to="menu_images/"), blank=True, null=True, verbose_name="Dish Image")

    created_at = models.DataTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - ₹{self.price}"