from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    favorite_color = models.TextField(null=True)

    def __str__(self):
        return self.email