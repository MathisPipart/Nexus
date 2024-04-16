from django.shortcuts import render


# Create your views here.
def vueProfil(request):
    return render(request, "profil.html")
