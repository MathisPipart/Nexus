from django.db import models
from django.utils import timezone
from datetime import datetime

class Post(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_de_creation = models.DateTimeField(default=timezone.now) 
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.titre
