from feed.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SubscribeForm
from .models import Info_Clubs
from django.http import JsonResponse


def vueClubs(request):
    clubs = Info_Clubs.objects.all()

    context = {
        'clubs': clubs,
    }
    for club in clubs:
        club.is_user_subscribed = request.user in club.membres.all()

    return render(request, "clubs.html", context)


def club_details(request, club_type):
    clubs = Info_Clubs.objects.all().filter(nom=club_type).first()
    posts = Post.objects.filter(club=clubs).order_by('-date_de_creation')
    #posts = Post.objects.all().order_by('-date_de_creation')
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
        form = SubscribeForm(request.POST)
        if form.is_valid():
            club = form.cleaned_data['club']
            club.membres.add(request.user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'}, status=200)
            return redirect('some_success_page')
    else:
        form = SubscribeForm()
    return render(request, 'subscribe.html', {'form': form})

@login_required
def unsubscribe_to_club(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            club = form.cleaned_data['club']
            club.membres.remove(request.user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'}, status=200)
            return redirect('some_success_page')
    else:
        form = SubscribeForm()
    return render(request, 'subscribe.html', {'form': form})