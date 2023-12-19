from django.contrib import admin
from .models import Utilisateur
from .models import Club

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Club)