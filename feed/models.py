from django.db import models

# Create your models here.

class Feed(models.Model):
    text = models.TextField()
