from django.db import models
from accessPoints.models import accessPoint
from users.models import user

# Create your models here.
class schedule(models.Model):

    start_time = models.TimeField()
    end_time = models.TimeField()
    access_point = models.ManyToManyField(accessPoint )
    user = models.ForeignKey(user, on_delete=models.CASCADE)

