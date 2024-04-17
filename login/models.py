from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user', 'User'
    SUPERUSER = 'superuser', 'Superuser'
    MODERATOR = 'moderator', 'Moderator'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER
    )

