function toggleHeart() {
    var likeIcon = document.getElementById('likeIcon');
    var emptyHeart = likeIcon.getAttribute('coeurVide');
    var filledHeart = likeIcon.getAttribute('coeurRouge');

    if (likeIcon.src.includes('coeur_vide')) {
        likeIcon.src = filledHeart;
    } else {
        likeIcon.src = emptyHeart;
    }

    likeIcon.style.transform = 'scale(1.2)';
    setTimeout(function() {
        likeIcon.style.transform = 'scale(1)';
    }, 200);

    // TODO: Ajoutez ici le code pour mettre à jour l'état du "like" sur le serveur
}
