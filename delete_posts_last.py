import os
from django.core.wsgi import get_wsgi_application

# Définissez la variable DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")

# Chargez les paramètres de Django
application = get_wsgi_application()

# Importez le modèle de votre post
from feed.models import Post

def delete_last_posts():
    # Récupérez tous les posts de la base de données
    posts = Post.objects.all()

    # supprimer le desnier post en date
    posts.last().delete()
    print("Le dernier post a été supprimé de la base de données.")

if __name__ == "__main__":
    delete_last_posts()


