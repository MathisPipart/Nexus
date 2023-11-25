from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings

class Post(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_de_creation = models.DateTimeField(default=timezone.now) 
    image = models.ImageField(upload_to='', blank=True, null=True,)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.titre