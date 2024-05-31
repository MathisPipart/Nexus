from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from clubs.models import Info_Clubs


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
    club = models.ForeignKey(Info_Clubs, on_delete=models.CASCADE, blank=True, null=True)

    def get_subscribed_clubs(self):
        return self.user.clubs_subscribed.all()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)