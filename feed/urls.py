from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="feed"),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('err404', views.err404, name='err404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
