from django.urls import path
from . import views

urlpatterns = [
    path("", views.vueClubs, name="vueClubs"),
    path('club_details/<str:club_type>/', views.club_details, name='club_details'),
    path('subscribe/', views.subscribe_to_club, name='subscribe_to_club'),
    path('unsubscribe/', views.unsubscribe_to_club, name='unsubscribe_to_club'),
]
