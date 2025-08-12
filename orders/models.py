from django.db import models

# Create your models here.
from django.db import models

class RestaurantInfo(models.model):
    name = models.charfield(max_length=255)
    phone = models.chharfield(max_length=15)