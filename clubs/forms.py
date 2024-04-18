from django import forms
from .models import Info_Clubs


class SubscribeForm(forms.Form):
    club = forms.ModelChoiceField(queryset=Info_Clubs.objects.all(), required=True, label="Choisir un club")
