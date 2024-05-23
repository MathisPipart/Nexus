from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Message
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_messages(user=request.user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user']
        directs = Message.objects.filter(user=user, recipient=message['user'])
        directs.update(is_read=True)

    for message in messages:
        if message['user'].id == active_direct.id:
            message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct
    }

    return render(request, "inbox.html", context)

def directs_messages(request, user_id):
    user = request.user
    messages = Message.get_messages(user=user)
    # active_direct = username
    # directs = Message.objects.filter(user=user, recipient__username=username)
    active_direct = get_object_or_404(User, id=user_id)
    directs = Message.objects.filter(user=request.user, recipient=active_direct)
    directs.update(is_read=True)

    for message in messages:
        if message['user'].id == active_direct.id:
            message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct
    }

    return render(request, "inbox.html", context)


def send_direct_message(request):
    # from_user = request.user
    # to_user_username = request.POST.get('to_user')
    # body = request.POST.get('body')

    # if request.method == "POST":
    #     to_user = User.objects.get(username=to_user_username)
    #     Message.send_message(from_user, to_user, body)
    #     return redirect('inbox')

    if request.method == "POST":
        print("POST data:", request.POST)
        from_user = request.user
        to_userid = request.POST.get('to_user')
        body = request.POST.get('body')

        # vérification que to_user_userid est un entier valide et non vide
        try:
            to_user_id = int(to_userid)
        except (ValueError, TypeError):
            return redirect('inbox')

        # get_object_or_404 pour éviter User.DoesNotExist
        to_user = get_object_or_404(User, id=to_user_id)

        # Envoi du message
        Message.send_message(from_user, to_user, body)

        # construction de l'url pour rester dans la conv
        conversation_url = reverse('directs_messages', kwargs={'user_id': to_user_id})
        return redirect(conversation_url)


def user_search(request):
    query = request.GET.get('q') # recupération de la valeur de la requete
    context = {}

    # si une requete, on cherche dans la bdd, et filtre les users par nom ou prenom
    if query:
        users = User.objects.filter(Q(first_name__icontains=query))
        users2 = User.objects.filter(Q(last_name__icontains=query))
        users = users.union(users2)

        # Paginator : pour faire une pagination affichant les users 8 par 8 si on trouve bcp de personnes
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator
        }

    return render(request, "search.html", context)
