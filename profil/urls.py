from django.urls import path
from . import views

urlpatterns = [
    path("", views.vueProfil, name="vueProfil"),
]