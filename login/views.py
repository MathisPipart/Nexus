from django.shortcuts import render, redirect
from django.contrib.auth import logout
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


# Create your views here.
def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("/")


"""def vueLogin(request):
    return render(request, "login.html")"""
