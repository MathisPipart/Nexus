from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Post
import os

def home(request):
    posts = Post.objects.all()
    return render(request, "feed.html", {'posts': posts})

def run_script(request):
    os.system('python add_posts.py')
    result = "Script exécuté avec succès."
    return JsonResponse({'message': result})
