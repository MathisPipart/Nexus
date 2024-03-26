from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post, Image
from .forms import AddPost
from django.contrib.auth.decorators import login_required
import os


@login_required
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

    else:
        posts = Post.objects.all()
        posts_size = len(posts)
        posts = reversed(posts)
        form = AddPost()

    return render(request, "feed.html", {'posts': posts, 'form': form, 'posts_size': posts_size})


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
