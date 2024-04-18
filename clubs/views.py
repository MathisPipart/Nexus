from feed.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SubscribeForm
from .models import Info_Clubs


def vueClubs(request):
    clubs = Info_Clubs.objects.all()

    context = {
        'clubs': clubs,
    }

    return render(request, "clubs.html", context)


def club_details(request, club_type):
    clubs = Info_Clubs.objects.all().filter(nom=club_type).first()

    posts = Post.objects.all().order_by('-date_de_creation')
    posts_size = len(posts)
    posts = reversed(posts)

    context = {
        'clubs': clubs,
        'posts': posts, 
        'posts_size': posts_size, 
    }

    return render(request, "club_details.html", context)

@login_required
def subscribe_to_club(request):
    if request.method == 'POST':
        club_id = request.POST.get('club_id')
        club = Info_Clubs.objects.get(id=club_id)
        club.membres.add(request.user)
        return redirect('vueClubs')
    else:
        return render(request, '404.html')


