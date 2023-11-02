from django.shortcuts import render, HttpResponse
from .models import Feed

# Create your views here.
def home(request):
    return render(request, "feed.html")

def my_view(request):
    feed = Feed(["Bonjour, il s'agit d'un modèle de post", "Pierre va payer sa tournée de cookies gourmands", "Il faudrait commencer à bosser pour les examens et avancer sur Schooding"])
    return render(request, 'feed.html', {'feed': feed})
