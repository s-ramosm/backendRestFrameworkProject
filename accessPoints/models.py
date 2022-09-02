
from django.db import models
from companies.models import company

# Create your models here.

class accessPoint(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    company_id = models.ForeignKey(company,on_delete=models.CASCADE)
    active = models.BooleanField()