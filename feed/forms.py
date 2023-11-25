from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField 

class AddPost(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100, 
                            widget=forms.TextInput(
                                attrs={'title': 'Titre du post','placeholder': 'Titre du post'}))
    
    contenu = forms.CharField(widget=CKEditorWidget(config_name='default'))
    
    image = forms.ImageField(required=False, 
                            widget=forms.FileInput(
                                attrs={'title': 'Image du post', 'placeholder': 'Image du post'},
                                ))
