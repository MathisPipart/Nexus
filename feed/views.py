from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post
from .forms import AddPost
import os

def home(request):
    if request.method == "POST" : 
        form = AddPost(request.POST)

        if form.is_valid():
            titre = form.cleaned_data["titre"]
            contenu = form.cleaned_data["contenu"]
            nouveau_post = Post(
                titre = titre,
                contenu = contenu,
            )
            nouveau_post.save()
            posts = Post.objects.all()
            form = AddPost()
            return HttpResponseRedirect("/")
            # return render(request, "feed.html", {'posts': posts, 'form': form})

    else :    
        posts = Post.objects.all()
        posts = reversed(posts)
        form = AddPost()

    return render(request, "feed.html", {'posts': posts, 'form': form})