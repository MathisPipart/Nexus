import os
from django.core.wsgi import get_wsgi_application

# Définissez la variable DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")

# Chargez les paramètres de Django
application = get_wsgi_application()

# Importez le modèle de votre post
from feed.models import Post

def lister_titres_posts():
    # Récupérez tous les posts de la base de données
    posts = Post.objects.all()
        
    if not posts.exists():
        print("Il n'y a pas de posts dans la base de données.")
        return
    else : 
        print("Il y a {} posts dans la base de données.".format(posts.count()))

    # Parcourez les posts et affichez leurs titres
    for post in posts:
        print(post.titre)

if __name__ == "__main__":
    lister_titres_posts()
