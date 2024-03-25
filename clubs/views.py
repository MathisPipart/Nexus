from django.shortcuts import render

# Create your views here.
def vueClubs(request):
    return render(request, "clubs.html")

def club_musique(request):
    return render(request, "club_musique.html")