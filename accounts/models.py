from django.contrib.auth.models import AbstractUser
from django.db import models

# Creating our models
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
