document.addEventListener('DOMContentLoaded', function() {
    // CHECKBOX NOTIFICATIONS
    var ligneNotification = document.getElementById('notification');
    ligneNotification.addEventListener('click', function(event) {
        event.stopPropagation(); // Prévenir la propagation de l'événement pour ne pas cocher/décocher deux fois si le clic est directement sur le checkbox
        var checkboxNotif = document.getElementById('checkboxNotif');
        checkboxNotif.checked = !checkboxNotif.checked; // Inverser l'état du checkbox
    });

    // Pour arrêter la propagation du clic direct sur le checkbox de notifications
    document.getElementById('checkboxNotif').addEventListener('click', function(event) {
        event.stopPropagation();
    });

    // CHECKBOX SON
    var ligneSon = document.getElementById('son');
    ligneSon.addEventListener('click', function(event) {
        event.stopPropagation(); // Prévenir la propagation de l'événement
        var checkboxSon = document.getElementById('checkboxSon');
        checkboxSon.checked = !checkboxSon.checked; // Inverser l'état du checkbox
    });

    // Pour arrêter la propagation du clic direct sur le checkbox de son
    document.getElementById('checkboxSon').addEventListener('click', function(event) {
        event.stopPropagation();
    });


});

