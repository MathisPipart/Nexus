from django.urls import path
from . import views

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("directs/<int:user_id>", views.directs_messages, name="directs_messages"),
    path("send/", views.send_direct_message, name="send_direct_message"),
    path("new/", views.user_search, name="user_search")
]