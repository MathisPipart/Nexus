from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from clubs.models import Info_Clubs


class AddPost(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100, 
                            widget=forms.TextInput(
                                attrs={'title': 'Titre du post','placeholder': 'Titre du post'}))
    
    contenu = forms.CharField(required=True, widget=CKEditorWidget(config_name='default', attrs={'placeholder': 'Contenu du post'}))

    file_field = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True,
                                                                        'title': 'multiple images',
                                                                        'accept': 'image/*',
                                                                        }))
    
    club = forms.ModelChoiceField(queryset=Info_Clubs.objects.all(), required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddPost, self).__init__(*args, **kwargs)
        if user and hasattr(user, 'userprofile'):
            self.fields['club'].initial = user.userprofile.club