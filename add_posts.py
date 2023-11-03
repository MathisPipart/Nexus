import os
from django.core.wsgi import get_wsgi_application

# Définissez la variable DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus.settings")

# Chargez les paramètres de Django
application = get_wsgi_application()

# Importez le modèle de votre post
from feed.models import Post

# Créez une instance du modèle avec les détails du post
nouveau_post = Post(
    titre="Ma",
    contenu="🎉 Rejoignez-nous pour la WINTER NIGHT ❄️! 🎉 <br> Le BDE vous convie à notre soirée étudiante hivernal : la WINTER NIGHT. Venez célébrer avec nous, profiter de la musique, des boissons et de la bonne compagnie. <br/> Nous vous attendons nombreux le 03/11/2023 à l'école à partir de 22h30. Ne manquez pas cet événement exceptionnel ! 🌟 "
)

# Enregistrez le post dans la base de données
nouveau_post.save()

# Imprimez un message pour indiquer que le post a été ajouté
print("Le post a été ajouté à la base de données.")
