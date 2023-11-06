from django.db import models
from django.utils import timezone
from datetime import datetime

class Post(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_de_creation = models.DateTimeField(default=timezone.now)  # Importez timezone au début de votre fichier models.py

    def __str__(self):
        return self.titre
