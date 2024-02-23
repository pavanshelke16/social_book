from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .manager import CustomUserManager  
from django.core.validators import validate_email



class CustomUser(AbstractUser):
    email = models.EmailField(validators=[validate_email])
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


class UploadedFile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    year_published = models.IntegerField()

    def __str__(self):
        return self.title

