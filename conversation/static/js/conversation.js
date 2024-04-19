document.addEventListener("DOMContentLoaded", function() {
    // Récupération de la popup et du bouton pour l'ouvrir
    var popup = document.getElementById("myPopup");
    var btnOpenPopup = document.getElementById("myBtt");
    
    // Récupération du bouton pour fermer la popup
    var btnClosePopup = popup.querySelector(".close");

    // Ajout d'un écouteur d'événement pour ouvrir la popup lorsque le bouton est cliqué
    btnOpenPopup.addEventListener("click", function() {
        popup.style.display = "block";
    });

    // Ajout d'un écouteur d'événement pour fermer la popup lorsque le bouton de fermeture est cliqué
    btnClosePopup.addEventListener("click", function() {
        popup.style.display = "none";
    });

    // Fermer la popup si l'utilisateur clique en dehors de celle-ci
    window.addEventListener("click", function(event) {
        if (event.target == popup) {
            popup.style.display = "none";
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Récupération de tous les boutons correspondant aux conversations
    var conversationButtons = document.querySelectorAll('.conversation');

    // Ajout d'un écouteur d'événement de clic à chaque bouton
    conversationButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Récupération de l'ID de la conversation à partir de l'attribut data
            var conversationId = button.dataset.conversationId;

            // Envoi d'une requête AJAX pour récupérer les messages de cette conversation
            fetch('/conversation/messages/' + conversationId)
                .then(response => response.json())
                .then(data => {
                    // Mise à jour du contenu de messages_container avec les messages récupérés
                    var messagesContainer = document.getElementById('messages_container');
                    messagesContainer.innerHTML = ''; // Effacer le contenu actuel
                    data.forEach(function(message) {
                        var messageElement = document.createElement('p');
                        messageElement.textContent = message.contenu + ' - Auteur: ' + message.auteur;
                        messagesContainer.appendChild(messageElement);
                    });
                })
                .catch(error => {
                    console.error('Error fetching messages:', error);
                });
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var messageForm = document.getElementById('messageForm');
    messageForm.addEventListener('submit', function(event) {
        print("iciiiiiiiiiiii !!!!!!");
        event.preventDefault(); // Empêche la soumission du formulaire par défaut
        
        // Récupération des données du formulaire
        var formData = new FormData(messageForm);
        
        // Création de la requête AJAX
        var xhr = new XMLHttpRequest();
        xhr.open('POST', ''); // Envoie la requête POST vers la même page actuelle
        xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); // Ajout du jeton CSRF
        
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Réussite de la requête, vous pouvez ajouter un traitement supplémentaire ici si nécessaire
                console.log('Message envoyé avec succès');
                // Vous pouvez également rafraîchir la liste des messages si nécessaire
            } else {
                // Gestion des erreurs
                console.error('Erreur lors de l\'envoi du message');
            }
        };
        
        xhr.send(formData); // Envoi des données du formulaire via AJAX
    });
});
