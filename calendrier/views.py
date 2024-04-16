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

def vueCalendrier(request):
    form = URLForm(request.POST or None)
    if form.is_valid():
        #ical_url = "https://planif.esiee.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=3346,4195&projectId=11&calType=ical&nbWeeks=52"
        # https://planif.esiee.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=1543,1788&projectId=11&calType=ical&nbWeeks=52               E3FI
        ical_url = form.cleaned_data['url']
        importEvent(ical_url)
        events = Event.objects.all()
        return render(request, "calendrier.html", {"events": events, "form": form})
    else:
        form = URLForm()
    return render(request, "calendrier.html", {"form": form})




"""def importEvent(url):
    req = requests.get(url)
    cal = Calendar.from_ical(req.text)

    for component in cal.walk():
        if component.name == "VEVENT":
            # Vérifiez si l'événement existe déjà pour éviter les doublons
            _, created = Event.objects.get_or_create(
                title=component.get('summary'),
                defaults={
                    'description': component.get('description', ''),
                    'start_time': component.get('dtstart').dt,
                    'end_time': component.get('dtend').dt,
                }
            )"""

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
