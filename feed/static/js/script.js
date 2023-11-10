//alert("Max la saucisse");

console.log("Max la saucisse");

function myFunction(button) {
    var target = $(button).attr('data-target');
    console.log("data-target value: " + target);

    var x = document.getElementsByClassName(target);

    var posts = document.getElementsByClassName("f_posts");

    // si le target est f_events_search on caches les posts et les conversations et on affiche les events
    if (target == "f_events_search") {
        for (var i = 0; i < posts.length; i++) {
            posts[i].style.display = "none";
        }
        for (var i = 0; i < x.length; i++) {
            x[i].style.display = "block";
        }
        var conversations = document.getElementsByClassName("f_conversations");
        for (var i = 0; i < conversations.length; i++) {
            conversations[i].style.display = "none";
        }
    }

    // si le target est f_conversations on caches les posts et les events et on affiche les conversations
    if (target == "f_conversations") {
        for (var i = 0; i < posts.length; i++) {
            posts[i].style.display = "none";
        }
        for (var i = 0; i < x.length; i++) {
            x[i].style.display = "block";
        }
        var events = document.getElementsByClassName("f_events_search");
        for (var i = 0; i < events.length; i++) {
            events[i].style.display = "none";
        }
    }

    // si le target est f_posts on caches les conversations et les events et on affiche les posts
    if (target == "f_posts") {
        for (var i = 0; i < x.length; i++) {
            x[i].style.display = "block";
        }
        var events = document.getElementsByClassName("f_events_search");
        for (var i = 0; i < events.length; i++) {
            events[i].style.display = "none";
        }
        var conversations = document.getElementsByClassName("f_conversations");
        for (var i = 0; i < conversations.length; i++) {
            conversations[i].style.display = "none";
        }
    }
}

// Fonction pour réafficher tous les blocs
function showAllBlocks() {
    var posts = document.getElementsByClassName("f_posts");
    var events = document.getElementsByClassName("f_events_search");
    var conversations = document.getElementsByClassName("f_conversations");
    
    if (window.innerWidth < 768) {
        // Si la largeur de la fenêtre est inférieure à 768 pixels (ajustez la valeur seuil selon vos besoins)
        for (var i = 0; i < posts.length; i++) {
            posts[i].style.display = "block";
        }
        for (var i = 0; i < events.length; i++) {
            events[i].style.display = "none";
        }
        for (var i = 0; i < conversations.length; i++) {
            conversations[i].style.display = "none";
        }
    } else {
        // Si la largeur de la fenêtre est supérieure ou égale à 768 pixels
        for (var i = 0; i < posts.length; i++) {
            posts[i].style.display = "block";
        }
        for (var i = 0; i < events.length; i++) {
            events[i].style.display = "block";
        }
        for (var i = 0; i < conversations.length; i++) {
            conversations[i].style.display = "block";
        }
    }
}

// function launchPythonScript() {
//         // Code pour lancer le script Python
//         alert("Script Python lancé!"); // Remplacez ceci par votre code réel
// }

document.getElementById("run-script-btn").addEventListener("click", function() {

    alert("- START -");

    fetch('/run-script/')
    .then(response => response.json())
    .then(data => alert(data.message));

    alert("- END -");
});

// Ajouter un gestionnaire d'événement pour l'événement de redimensionnement de la fenêtre
window.addEventListener('resize', function() {
    // Réafficher les blocs en fonction de la largeur de la fenêtre
    showAllBlocks();
});

// Appelez la fonction showAllBlocks pour afficher les blocs au chargement de la page
showAllBlocks();
