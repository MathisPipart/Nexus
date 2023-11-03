from django.shortcuts import render

# Create your views here.
def vueClassement(request):
    return render(request, "classement.html")