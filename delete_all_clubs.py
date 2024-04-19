from faker import Faker
from django.core.files.base import ContentFile
import base64
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")
application = get_wsgi_application()

from clubs.models import Info_Clubs


def delete_all_clubs():
    clubs = Info_Clubs.objects.all()

    for club in clubs:
        club.delete()

    print("Tous les clubs ont été supprimés.")


if __name__ == "__main__":
    delete_all_clubs()
