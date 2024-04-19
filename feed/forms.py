from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from clubs.models import Info_Clubs


class AddPost(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100, 
                            widget=forms.TextInput(
                                attrs={'title': 'Titre du post','placeholder': 'Titre du post'}))
    
    contenu = forms.CharField(widget=CKEditorWidget(config_name='default'))
    
    # image = forms.ImageField(required=False,
    #                         widget=forms.FileInput(
    #                             attrs={'title': 'Image du post',
    #                                     'placeholder': 'Image du post'},))

    file_field = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True,
                                                                        'title': 'multiple images',
                                                                        'accept': 'image/*',
                                                                        }))
    club = forms.ModelChoiceField(queryset=Info_Clubs.objects.all(), required=False, widget=forms.Select(attrs={'title': 'Club du post', 'placeholder': 'Club du post'}))

# limit the type of file to be uploaded to images only
    # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,
    #                                                                     'title': 'multiple images',
    #                                                                     'accept': 'image/*'
    #                                                                     }))


    # image = forms.FileField(required=False, widget = forms.TextInput(attrs={
    #     'title': 'Image du post', 
    #     'placeholder': 'Image du post',
    #     "type": "File",
    #     "class": "form-control",
    #     "multiple": "True",
    # }), label = "IMAGE")