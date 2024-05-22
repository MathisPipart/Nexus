from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.contrib.auth.decorators import user_passes_test


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
    membres = models.ManyToManyField(User, through='Subscription', related_name='clubs_subscribed')
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom + " " + self.description + " " + self.president + " " + self.vp1 + " " + self.vp2 + " " + self.secretaire + " " + self.tresorier

    def get_all_fields(self):
        return model_to_dict(self)


class Subscription(models.Model):
    club = models.ForeignKey(Info_Clubs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_subscribed = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('club', 'user')  # A user can only subscribe once to a club

    def __str__(self):
        return f"{self.user.username} subscribed to {self.club.nom}"
