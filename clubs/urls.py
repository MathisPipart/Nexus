from django.urls import path
from . import views

urlpatterns = [
    path("", views.vueClubs, name="vueClubs"),
    path('club_details/<str:club_type>/', views.club_details, name='club_details'),
]