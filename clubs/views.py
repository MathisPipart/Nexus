from django.shortcuts import render
from feed.models import Post  # Import the Post model


def vueClubs(request):
    return render(request, "clubs.html")



def club_details(request):
    posts = Post.objects.all().order_by('-date_de_creation')
    posts_size = len(posts)
    posts = reversed(posts)
    
    return render(request, "club_details.html", {'posts': posts, 'posts_size': posts_size})