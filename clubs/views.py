from django.shortcuts import render
from feed.models import Post 
from django.shortcuts import render
from .models import Info_Clubs


def vueClubs(request):
    clubs = Info_Clubs.objects.all()
    return render(request, "clubs.html", {'clubs': clubs})


def club_details(request, club_type):
    posts = Post.objects.all().order_by('-date_de_creation')
    posts_size = len(posts)
    posts = reversed(posts)
    return render(request, "club_details.html", {'posts': posts, 'posts_size': posts_size, 'club_type': club_type})
