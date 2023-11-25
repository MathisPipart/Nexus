from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post
from .forms import AddPost
import os

def home(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES) 

        if form.is_valid():
            titre = form.cleaned_data["titre"]
            contenu = form.cleaned_data["contenu"]
            image = form.cleaned_data.get("image")
            nouveau_post = Post(
                titre = titre,
                contenu = contenu,
                image = image 
            )
            nouveau_post.save()
            posts = Post.objects.all()
            form = AddPost()
            return HttpResponseRedirect("/")

    else:
        posts = Post.objects.all()
        posts = reversed(posts)
        form = AddPost()

    return render(request, "feed.html", {'posts': posts, 'form': form})

def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        # delete the image file
        if post.image:
            os.remove(post.image.path)
        return HttpResponseRedirect('/')