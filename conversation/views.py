from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Conversation, Message
from .forms import ConversationForm, MessageForm

def create_conversation(request):
    # Récupérer l'ID de l'utilisateur à partir de la requête
    user_id = request.user.id
    default_id = 123  # ID par défaut de la conversation
    
    # Récupérer toutes les conversations associées à l'utilisateur avec cet ID
    conversations = Conversation.objects.filter(users__id=user_id)
    if request.method == 'POST':
        form = ConversationForm(request.POST, current_user=request.user, default_id=default_id)
        msgForm = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ConversationForm(current_user=request.user, default_id=default_id)
    return render(request, 'conversation.html', {'form': form, 'conversations': conversations})

def view_conversation_messages(request, conversation_id):
    # Récupérer la conversation associée à l'ID fourni
    conversation = get_object_or_404(Conversation, id=conversation_id)
    
    # Récupérer tous les messages liés à cette conversation
    messages = Message.objects.filter(conversation=conversation)
    
    return render(request, 'conversation.html', {'conversation': conversation, 'messages': messages})

def get_conversation_messages(request, conversation_id):
    # Récupérer les messages associés à la conversation
    messages = Message.objects.filter(conversation_id=conversation_id).values('contenu', 'auteur__username')
    
    # Convertir les messages en liste JSON et les renvoyer
    return JsonResponse(list(messages), safe=False)

