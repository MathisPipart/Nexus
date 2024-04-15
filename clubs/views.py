from django.shortcuts import render
from feed.models import Post  # Import the Post model
from django.shortcuts import render


def vueClubs(request):
    return render(request, "clubs.html")


def club_details(request, club_type):
    context = {
        'club_type': club_type
    }
    return render(request, 'club_details.html', context)
