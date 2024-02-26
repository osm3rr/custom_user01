from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here my friend :).

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
