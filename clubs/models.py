from django.db import models

# Create your models here.
class Info_Clubs(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    description = models.TextField()
    banniere = models.ImageField(upload_to='clubs/')
    photo = models.ImageField(upload_to='clubs/')
    president = models.CharField(max_length=50)
    vp1 = models.CharField(max_length=50)
    vp2 = models.CharField(max_length=50)
    vp3 = models.CharField(max_length=50, blank=True)
    secretaire = models.CharField(max_length=50)
    secretaire2 = models.CharField(max_length=50, blank=True)
    tresorier = models.CharField(max_length=50)
    tresorier2 = models.CharField(max_length=50, blank=True)

    
    def __str__(self):
        return f"{self.nom} - {self.description}"

        return self.nom + " " + self.description + " " + self.banniere + " " + self.photo + " " + self.president + " " + self.vp1 + " " + self.vp2 + " " + self.secretaire + " " + self.tresorier