from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    contenu = models.TextField()
    users = models.ManyToManyField(User, blank=True)

@receiver(post_save, sender=Conversation)
def add_current_user_to_conversation(sender, instance, created, current_user=None, **kwargs):
    if created:
        # Assuming you have access to the current user instance somehow
        # For example, if you are handling this in a view, you can access it through request.user
        # Here, I'll assume you have a variable called 'current_user' that holds the current user instance
        instance.users.add(current_user)