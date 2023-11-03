from django.shortcuts import render
from icalendar import Calendar
import requests
from .models import Event
from django.utils import timezone

# Create your views here.
def vueCalendrier(request):
    events = Event.objects.all()
    return render(request, "calendrier.html", {"events": events})

def importEvent(url):
    req = requests.get(url)
    cal = Calendar.from_ical(req.text)

    for component in cal.walk():
        if component.name == "VEVENT":
            Event.objects.create(
                title = component.get('summary'),
                description = component.get('description', ''),
                start_time = component.get('dtstart').dt,
                end_time = component.get('dtend').dt,
            )





