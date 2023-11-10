import os
from django.core.wsgi import get_wsgi_application
import datetime
from django.utils import timezone

# Définissez la variable DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")

# Chargez les paramètres de Django
application = get_wsgi_application()

# Importez le modèle de votre post
from feed.models import Post
import random
import string

def add_posts():
    # Créez une instance du modèle avec les détails du post

    #generate random title and random content
    
    nouveau_post = Post(
        titre = "Max ",
        contenu = "Merci pour les dragibus <3",
        date_de_creation=timezone.now()
    )

    # Enregistrez le post dans la base de données
    nouveau_post.save()

    # Imprimez un message pour indiquer que le post a été ajouté
    print("Le post a été ajouté à la base de données.")

if __name__ == "__main__":
    add_posts()