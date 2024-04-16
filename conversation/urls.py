from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_conversation, name='conversation'),
    path('messages/<int:conversation_id>/', views.get_conversation_messages, name='conversation_messages'),
]
