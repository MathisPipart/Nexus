from django.shortcuts import render
from .models import Utilisateur
from .models import Club

# Create your views here.
def vueClassement(request):
    utilisateurs = Utilisateur.objects.all().order_by('-score')
    clubs = Club.objects.all().order_by('-score')
    context = {
        'utilisateurs': utilisateurs,
        'premier_utilisateur': utilisateurs[0] if len(utilisateurs) > 0 else None,
        'deuxieme_utilisateur': utilisateurs[1] if len(utilisateurs) > 1 else None,
        'troisieme_utilisateur': utilisateurs[2] if len(utilisateurs) > 2 else None,

        'clubs': clubs,
        'premier_club': clubs[0] if len(clubs) > 0 else None,
        'deuxieme_club': clubs[1] if len(clubs) > 1 else None,
        'troisieme_club': clubs[2] if len(clubs) > 2 else None,
    }
    return render(request, "classement.html", context)