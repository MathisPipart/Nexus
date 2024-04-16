from django.shortcuts import render, redirect
from .models import Conversation
from .forms import ConversationForm

def create_conversation(request):
    # Récupérer l'ID de l'utilisateur à partir de la requête
    user_id = request.user.id
    default_id = 123  # ID par défaut de la conversation
    
    # Récupérer toutes les conversations associées à l'utilisateur avec cet ID
    conversations = Conversation.objects.filter(users__id=user_id)
    if request.method == 'POST':
        form = ConversationForm(request.POST, current_user=request.user, default_id=default_id)
        if form.is_valid():
            form.save()
    else:
        form = ConversationForm(current_user=request.user, default_id=default_id)
    return render(request, 'conversation.html', {'form': form, 'conversations': conversations})