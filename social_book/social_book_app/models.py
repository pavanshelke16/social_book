from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .manager import CustomUserManager  

class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.birth_year:
            current_year = timezone.now().year
            self.age = current_year - self.birth_year

        super().save(*args, **kwargs)
