from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):

    email = models.EmailField( unique=True)
    is_owner = models.BooleanField(default=False)
