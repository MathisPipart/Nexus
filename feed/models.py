from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings


class Post(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(blank=False, null=False, default=' ')
    date_de_creation = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey('clubs.Info_Clubs', on_delete=models.CASCADE, null=True)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')
