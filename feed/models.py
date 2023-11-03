from django.db import models

class Post(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

    def __str__(self):
        return self.titre