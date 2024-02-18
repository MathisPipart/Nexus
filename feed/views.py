from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post, Image
from .forms import AddPost
import os

def home(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES) 

        if form.is_valid():
            # Create and save the post instance
            post = Post(
                titre=form.cleaned_data['titre'],
                contenu=form.cleaned_data['contenu'])
            post.save()
            
            # Save each file as an Image instance linked to the post
            for f in request.FILES.getlist('file_field'):
                Image.objects.create(post=post, image=f)
            
            return HttpResponseRedirect('/')
        
        
        
        # if form.is_valid():
        #     titre = form.cleaned_data["titre"]
        #     contenu = form.cleaned_data["contenu"]
        #     image = form.cleaned_data.get("image")
        #     files = request.FILES.getlist('file_field')
        #     nouveau_post = Post(
        #         titre = titre,
        #         contenu = contenu,
        #         image = files
        #     )
        #     nouveau_post.save()
        #     posts = Post.objects.all()
        #     form = AddPost()
        #     return HttpResponseRedirect("/")

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
        if post.images:
            os.remove(post.image.path)
        return HttpResponseRedirect('/')
    
def modify_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.titre = request.POST['titre']
        post.contenu = request.POST['contenu']
        post.save()
        return HttpResponseRedirect('/')
    
def err404(request):
    return render(request, 'err404.html')