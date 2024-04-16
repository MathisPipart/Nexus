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
