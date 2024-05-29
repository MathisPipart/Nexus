from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post, Image
from .forms import AddPost
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
import os
from calendrier.models import Event


#@login_required
# To be added in prod
def home(request):
    posts = Post.objects.all()
    posts_size = len(posts)

    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            # Create and save the post instance
            post = Post(
                titre=form.cleaned_data['titre'],
                contenu=form.cleaned_data['contenu'],
                club=form.cleaned_data['club']
                )
            post.user = request.user
            post.save()

            # Save each file as an Image instance linked to the post
            for f in request.FILES.getlist('file_field'):
                Image.objects.create(post=post, image=f)

            return HttpResponseRedirect('/feed/')

    else:
        #posts = Post.objects.all()
        #posts_size = len(posts)
        #posts = reversed(posts)
        #form = AddPost()
        posts_subscribed = Post.objects.filter(club__membres=request.user).order_by('date_de_creation')
        posts_size = len(posts_subscribed)
        posts_subscribed = reversed(posts_subscribed)
        form = AddPost()

    events = Event.objects.all()

    return render(request, "feed.html", {"events": events, 'posts': posts_subscribed, 'form': form, 'posts_size': posts_size})



#@login_required
def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        for image in post.images.all():
            image.image.delete(save=False)
        post.delete()
        return HttpResponseRedirect('/feed/')


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
