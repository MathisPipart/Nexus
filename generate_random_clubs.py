from faker import Faker
from django.core.files.base import ContentFile
import base64
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")
application = get_wsgi_application()

from clubs.models import Info_Clubs

# Initialize the Faker library
fake = Faker()


def generate_random_clubs(n):
    for _ in range(n):
        # Generate fake data for each field
        nom = fake.word()
        description = fake.text()
        president = fake.name()
        vp1 = fake.name()
        vp2 = fake.name()
        vp3 = fake.name()
        secretaire = fake.name()
        secretaire2 = fake.name()
        tresorier = fake.name()
        tresorier2 = fake.name()

        # For the image fields, we'll just create a small dummy image
        # This is a 1x1 pixel black image encoded in base64
        dummy_image_content = b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='
        dummy_image_content = base64.b64decode(dummy_image_content)
        banniere = ContentFile(dummy_image_content, name=f'{nom}_banniere.png')
        photo = ContentFile(dummy_image_content, name=f'{nom}_photo.png')

        # Create the new club
        new_club = Info_Clubs(
            nom=nom,
            description=description,
            banniere=banniere,
            photo=photo,
            president=president,
            vp1=vp1,
            vp2=vp2,
            vp3=vp3,
            secretaire=secretaire,
            secretaire2=secretaire2,
            tresorier=tresorier,
            tresorier2=tresorier2,
        )
        new_club.save()


if __name__ == "__main__":
    generate_random_clubs(30)  # Generate 10 random clubs
