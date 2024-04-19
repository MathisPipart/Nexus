from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Conversation

class ConversationForm(forms.ModelForm):
    default_id = None  # ID par défaut pour la conversation

    class Meta:
        model = Conversation
        fields = ['contenu']

    def __init__(self, *args, current_user=None, default_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contenu'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contenu'})

        if current_user:
            self.current_user = current_user
        if default_id:
            self.default_id = default_id

    def save(self, commit=True):
        conversation = super().save(commit=False)
        if hasattr(self, 'current_user'):
            if commit:
                conversation.save()  # Sauvegarde de la conversation pour obtenir un ID valide
            conversation.users.add(self.current_user)  # Ajout de l'utilisateur après la sauvegarde de la conversation
        if commit:
            conversation.save()
        return conversation

class MessageForm(forms.Form):
    content = forms.CharField(label="Message", max_length=100,
                            widget=forms.TextInput(
                                attrs={'title': 'Titre du post', 'placeholder': 'votre Message...'}))
