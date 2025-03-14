
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self) -> str:
        return self.email
