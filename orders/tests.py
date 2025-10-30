from django.test import TestCase

# Create your tests here.
from django.db import models
from django.utils import timezone

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = model.DateField()
    valid_from =  models.DateField()

    def _str__(self):
        return f"{self.code} - {self.discount_percentage}%