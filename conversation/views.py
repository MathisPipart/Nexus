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

    # /!\ attention au risque de deux utilisateur avec le même username /!\
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

        # Assurez-vous que to_user_userid est un entier valide et non vide
        try:
            to_user_id = int(to_userid)
        except (ValueError, TypeError):
            # Vous pouvez ajouter une gestion d'erreur ici si l'ID n'est pas valide
            return redirect('inbox')

        # Utilisez get_object_or_404 pour éviter User.DoesNotExist
        to_user = get_object_or_404(User, id=to_user_id)

        # Envoi du message
        Message.send_message(from_user, to_user, body)

        conversation_url = reverse('directs_messages', kwargs={'user_id': to_user_id})
        return redirect(conversation_url)
    # else:
    #     # Si la méthode n'est pas POST, redirigez ou affichez une erreur appropriée
    #     return redirect('inbox')








