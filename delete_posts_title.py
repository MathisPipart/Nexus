import os
from django.core.wsgi import get_wsgi_application

# Définissez la variable DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")

# Chargez les paramètres de Django
application = get_wsgi_application()

# Importez le modèle de votre post
from feed.models import Post

def delete_post_tittle(): 
    posts = Post.objects.all()
    
    for post in posts:
        print(post.titre)

    titre = input("Quel est le titre du post a supprimer ? \n")

    if posts.exists():
        # supprimer le post
        post_a_supprimer = Post.objects.get(titre=titre)
        post_a_supprimer.delete()
        print("Le post a été supprimé de la base de données.")
    else:
        print("Le post n'existe pas dans la base de données.")
        #list des titres des posts disponibles
        for post in posts:
            print(post.titre)


if __name__ == "__main__":
    delete_post_tittle()
