from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="feed"),
    path("run-script/", views.run_script, name="run-script"),
]
