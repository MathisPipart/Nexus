from django.urls import path
from . import views

urlpatterns = [
    path("", views.vueLogin, name="vueLogin"),
]