import os
from django.core.wsgi import get_wsgi_application

# Définissez la variable DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")

# Chargez les paramètres de Django
application = get_wsgi_application()

# Importez le modèle de votre post
from feed.models import Post


def delete_all_posts():
    # Récupérez tous les posts de la base de données
    posts = Post.objects.all()

    # Parcourez les posts et affichez leurs titres
    for post in posts:
        post.delete()

    print("Tous les posts ont été supprimés de la base de données.")


if __name__ == "__main__":
    delete_all_posts()
