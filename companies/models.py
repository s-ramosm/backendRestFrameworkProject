from django.db import models
from countries.models import country
from states.models import state

# Create your models here.

class company(models.Model):

    nit = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    comercial_name = models.CharField(max_length=50) 
    number = models.IntegerField()
    email = models.EmailField(blank=False)
    website = models.CharField(max_length=50,blank=False)
    country_code = models.ForeignKey(country, on_delete=models.CASCADE)
    state =  models.ForeignKey(state, on_delete=models.CASCADE)




