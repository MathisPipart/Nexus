from django.urls import path
from . import views

urlpatterns = [
    path("", views.vueClubs, name="vueClubs"),
    path("club_musique", views.club_musique, name="club_musique"),
]
