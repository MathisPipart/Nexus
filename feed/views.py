from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post, Image
from .forms import AddPost
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
import os
from calendrier.models import Event
from conversation.models import Message


@login_required
# To be added in prod
def home(request):
    posts = Post.objects.all()
    posts_size = len(posts)
    messages = Message.get_messages(user=request.user)

    if request.method == "POST":
        form = AddPost(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            post = Post(
                titre=form.cleaned_data['titre'],
                contenu=form.cleaned_data['contenu'],
                # club=form.cleaned_data['club']
                club=request.user.userprofile.club
            )
            post.user = request.user
            post.save()

            for f in request.FILES.getlist('file_field'):
                Image.objects.create(post=post, image=f)

            return HttpResponseRedirect('/')

    else:
        posts_subscribed = Post.objects.filter(club__membres=request.user).order_by('date_de_creation')
        posts_size = len(posts_subscribed)
        posts_subscribed = reversed(posts_subscribed)
        form = AddPost(user=request.user)

    events = Event.objects.all()

    return render(request, "feed.html", {"events": events, 'posts': posts_subscribed, 'form': form, 'posts_size': posts_size, 'messages': messages})


@login_required
def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        for image in post.images.all():
            image.image.delete(save=False)
        post.delete()
        return HttpResponseRedirect('/')


# /!\ TODO :
# def modify_post(request, post_id):
#     if request.method == 'POST':
#         post = Post.objects.get(id=post_id)
#         post.titre = request.POST['titre']
#         post.contenu = request.POST['contenu']
#         post.save()
#         return HttpResponseRedirect('/')

def err404(request):
    return render(request, '404.html')
