from django.shortcuts import render

# Create your views here.
def vueCalendrier(request):
    return render(request, "calendrier.html")
