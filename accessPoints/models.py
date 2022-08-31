
from django.db import models

# Create your models here.

class accessPoint(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)