from django.shortcuts import render, redirect
from django.contrib.auth import logout
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    return render(request, "home.html")


def denied_access(request):
    return render(request, "closed.html")


def logout_view(request):
    logout(request)
    return redirect("/")
