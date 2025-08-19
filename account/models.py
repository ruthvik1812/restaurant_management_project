from django.db import models
from django.contrib.auth.models import User
# Create your models here
class UserProfile(models.model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=15)

    phone_number = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.name