from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="feed"),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    # path("run-script/", views.run_script, name="run-script"),
]
