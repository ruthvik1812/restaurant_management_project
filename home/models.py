from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Restaurant Name"
    )
    
    owner_name = models.CharField(
        max_length=255,
        verbose_name="Owner's Full Name"
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name="Contact Email"
    )
    
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Phone Number"
    )
    
    address = models.TextField(
        verbose_name="Complete Address"
    )
    
    city = models.CharField(
        max_length=100,
        verbose_name="City"
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

    class Meta:
        verbose_name ="Feedback"
        verbose_name_plural ="feedback"
        ordering =["-created_at"]
    
    def __str__(self):
        return self.comment[:50]

