from django.shortcuts import render

# Create your views here.


def vueLogin(request):
    return render(request, "login.html")