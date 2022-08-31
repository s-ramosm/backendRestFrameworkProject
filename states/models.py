from django.db import models
from countries.models import country
# Create your models here.

class state(models.Model):
    name = models.CharField(max_length=50, blank=False)
    country_id = models.ForeignKey(country, on_delete=models.CASCADE)