from django.shortcuts import render
from icalendar import Calendar
import requests
from .models import Event
from django.utils import timezone

# Create your views here.
def vueCalendrier(request):
    # URL du calendrier iCal fournie
    ical_url = "https://planif.esiee.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4195&projectId=11&calType=ical&nbWeeks=4"

    # Importer les événements depuis l'URL iCal
    importEvent(ical_url)

    # Récupérer les événements depuis la base de données
    events = Event.objects.all()

    # Envoyer les événements au template
    return render(request, "calendrier.html", {"events": events})


def importEvent(url):
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
            )






