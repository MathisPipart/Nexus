from django.shortcuts import render
from login.models import UserProfile
from clubs.models import Info_Clubs
from django.contrib.auth.decorators import login_required


@login_required
def vueClassement(request):
    utilisateurs = UserProfile.objects.all().order_by('score')
    utilisateurs = list(reversed(utilisateurs))
    clubs = Info_Clubs.objects.all()
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