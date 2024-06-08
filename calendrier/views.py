import datetime

from django.shortcuts import render, redirect
from icalendar import Calendar
import requests
from .models import Event
from django.utils import timezone
import os
import pytz
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import URLForm  # Assurez-vous d'importer URLForm de forms.py
from django.contrib.auth.decorators import login_required
from login.models import UserProfile


@login_required
def vueCalendrier(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = URLForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        ical_url = form.cleaned_data['url']
        user_profile.url = ical_url
        user_profile.save()
        importEvent(ical_url)
    elif user_profile.url:
        importEvent(user_profile.url)

    events = Event.objects.all()

    return render(request, "calendrier.html", {"events": events, "form": form, "url": user_profile.url})


@login_required
def importEvent(url):
    Event.objects.all().delete()
    # Télécharger le contenu iCal
    response = requests.get(url)
    response.raise_for_status()  # S'assurer que la requête a réussi

    # Parser le contenu iCal
    cal = Calendar.from_ical(response.content)

    # Parcourir les composants du calendrier
    for component in cal.walk():
        if component.name == "VEVENT":
            # Créer et sauvegarder un nouvel événement
            event = Event()
            event.title = str(component.get('summary'))
            event.description = str(component.get('description', ''))

            # Gérer les fuseaux horaires pour les dates de début et de fin
            start_dt = component.get('dtstart').dt
            end_dt = component.get('dtend').dt
            if not isinstance(start_dt, datetime.date):
                start_dt = pytz.UTC.localize(start_dt)
            if not isinstance(end_dt, datetime.date):
                end_dt = pytz.UTC.localize(end_dt)

            event.start_time = start_dt
            event.end_time = end_dt

            event.save()
