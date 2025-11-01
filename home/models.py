from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="RR Restaurant"
    )
    
    owner_name = models.CharField(
        max_length=255,
        verbose_name="Owner Name"
        default ="Ruthvik Raj chintala"
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
        default="ruthvikraj.chintala1812@gmail.com"
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
    opening_hours = models.JSONField(
        default=dict,
        verbose_name="Opening Hours",
        help_text="store opening hours in JSON format, eg. {'Mon-Fri': '10:00AM  - 11:00PM','Sat-Sun': '9:00 AM - 11:00PM'}"
    )

    logo = models.ImageField(
        upload_to="restaurant_logos/",
        blank=True,
        null=True,
        verbose_name="Restaurant Logo"
    )
     created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Registered On"
    )

    OPERATING_DAYS_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu' , 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    operating_hours = models.Charfield(
        max_length=50,
        help_text="Comma-separated list of operating days, e.g., 'Mon,Tue,Wed,Thu,Fri,Sat,Sun'",
        blank=True
    )
   def get_operating_days_list(self):
    """Return operating days as a list of strings """
    if self.operating_days:
        return self.operating_days.split(',')
        return []
        
class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
        ordering = ["-created_at"]

    def __str__(self):
    return f"{self.name} - {self.city}"
# Today's special Menu
class TodaySpecial(models.Model):
    name = models.CharField(max_length=200, verbose_name="Special Item Name")
    description = models.TextField(verbose_name="Special Item Description", blank="True", null="True")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to="specials/", blank=True, verbose_name="Special Dish Image")
    created_at = models.DateTimeField(auto_now_add=True)
    class Mete:
        verbose_name ="Today's Special
        verbose_name_plural= "Today's Specials"
        ordering = ['-created_at']
    def __str__(Self):
        return self.name
# Menu Model
class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.CASCADE,
        related_name="menu_items",
        verbose_name="Restaurant"
    )   
    name = models.CharField(
        max_length=100,
        verbose_name="Dish Name"
    )

    description = models.TextField(
    blank=True, null=True,
    verbose_name="Description"
    )
    price = models.DecimalField(
    max_digits=6,
    decimal_places=2,
    verbose_name="Price"
    )
    image = models.ImageField(
    upload_to="menu_images/",
    blank=True,
    null=True,
    verbose_name="Dish Image"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - ₹{self.price}"
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100,default="RR Restaurant")
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    
class Contact(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        created_at = models.DateTimeField(auto_now_add=True)
        def __str__(self):
        return self.name
class RestaurantLocation(models.Model):
    name = models.CharField(max_length=200, default= "RR Restaurant")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=200, default="+91 8639139326")
        
        def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"
# ----------------- CONTACTFORM --------------- #
class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

# ----------- FEEDBACK MODEL --------------------#
 class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Your Name")
    comment = models.TextField(verbose_name="Your Feedback")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted On")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        ordering = ["-submitted_at"]
    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime(%Y-%m-%d %H:%M')}"
# ----------- ABOUT CHEF --------------- #
class chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='chefs/',blank=True, null=True)

    def __str__(self):
        return self.name
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
class NutritionalInformation(models.Model):
    menu_item  = models.ForeignKey(
        'MenuItem',
        on_delete=models.CASCADE,
        related_name='nutritional_info'
    )
    calories = models.IntegerField()
    protein_grams = models.DecimalField(max_digits=5, decimal_places=2)
    fat_grams = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate_grams = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} - {self.calories} kcal"

    kjbmmmmmmmmmmkk
    kjjjkkjgjhhggggghgh
    kjjjjjgkjghasdfghjk
    wsdfghjklfhsfgjsghkmghdfcghbjnkmjliohjgv bmnmbnmbghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhv