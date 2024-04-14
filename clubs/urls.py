from django.urls import path
from . import views

urlpatterns = [
    path("", views.vueClubs, name="vueClubs"),
    path("club_details", views.club_details, name="club_details"),
]
