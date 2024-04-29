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

function toggleSave() {
    var saveIcon = document.getElementById('saveIcon');
    var emptySave = saveIcon.getAttribute('enregistrerVide');
    var filledSave = saveIcon.getAttribute('enregistrerRempli');

    if (saveIcon.src.includes('enregistrerVide')) {
        saveIcon.src = filledSave;
    } else {
        saveIcon.src = emptySave;
    }

    saveIcon.style.transform = 'scale(1.2)';
    setTimeout(function() {
        saveIcon.style.transform = 'scale(1)';
    }, 200);

    // TODO: Ajoutez ici le code pour mettre à jour l'état du "like" sur le serveur
}

function moveSendButton() {
    var sendButton = document.getElementById('envoieIcon');
    sendButton.style.position = 'absolute';
    sendButton.style.top = '10px'; // Ajustez cette valeur pour le positionnement vertical
    sendButton.style.right = '10px'; // Ajustez cette valeur pour le positionnement horizontal

    // Ajoutez un gestionnaire d'événements pour revenir à la position d'origine lors du clic
    sendButton.addEventListener('click', function() {
        sendButton.style.position = 'static';
        sendButton.style.top = 'auto';
        sendButton.style.right = 'auto';
    }, { once: true }); // Utilisez { once: true } pour que l'événement ne soit écouté qu'une seule fois
}
