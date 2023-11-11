from django import forms

class AddPost(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100)
    contenu = forms.CharField(label="Contenu", max_length=1000)