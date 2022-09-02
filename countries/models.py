from django.db import models

# Create your models here.
class country(models.Model):

    name = models.CharField(blank=False, max_length=50)
    code = models.IntegerField(primary_key=True, blank=False)
    description = models.CharField(max_length=50, blank=True)
