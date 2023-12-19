from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return self.nom + " " + self.prenom + " " + str(self.score)
    
class Club(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return self.nom + " " + " " + str(self.score)
