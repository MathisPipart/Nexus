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

function toggleCom() {
    var comIcon = document.getElementById('comIcon');

    comIcon.style.transform = 'scale(0.8)';
    setTimeout(function() {
        comIcon.style.transform = 'scale(1)';
    }, 200);
}


function moveSendButton() {
    var sendButton = document.getElementById('envoieIcon');
    sendButton.style.position = 'relative';
    sendButton.style.top = '-10px';
    sendButton.style.right = '-10px';
    sendButton.style.transition = 'transform 0.5s ease';

    setTimeout(function() {
        sendButton.style.transform = 'scale(0)';
    }, 100);

    setTimeout(function() {
        sendButton.style.position = 'static';
        sendButton.style.top = 'auto';
        sendButton.style.right = 'auto';
        sendButton.style.transform = 'scale(1)';
    }, 600);
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