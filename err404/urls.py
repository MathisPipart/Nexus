from django.urls import path
from . import views

urlpatterns = [
    path("", views.err404, name="err404"),
]