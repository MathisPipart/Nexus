from django.urls import path
from .views import reset_calendar_url
from . import views

urlpatterns = [
    path("", views.vueProfil, name="vueProfil"),
    path("reset_calendar_url", reset_calendar_url, name='reset_calendar_url'),
]