"""
URL configuration for Nexus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("feed.urls"), name="feed"),
    path("calendar/", include("calendrier.urls")),
    path("clubs/", include("clubs.urls")),
    path("ranking/", include("classement.urls")),
    path("profil/", include("profil.urls")),
    path("404/", include("err404.urls")),
    path('accounts/', include('allauth.urls')),
    path("login/", include('login.urls')),
    path("inbox/", include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
