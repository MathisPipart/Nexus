// alert("Max la saucisse");
// console.log("joel");
document.addEventListener('DOMContentLoaded', function() {
    var toggleCalendarCheckbox = document.getElementById('toggle-calendar');
    var calendarContainer = document.getElementById('calendar');
    toggleCalendarCheckbox.addEventListener('change', function() {
        calendarContainer.style.display = this.checked ? 'block' : 'none';
    });

    var toggleLoremCheckbox = document.getElementById('toggle-lorem');
    var loremText = document.querySelector('.lorem-text');
    toggleLoremCheckbox.addEventListener('change', function() {
        loremText.style.display = this.checked ? 'block' : 'none';
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    let calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'europe/Paris',
        initialView: 'listDay',
        height: 'auto',
        locale: 'fr',
        hiddenDays: [ 0 ],
        nowIndicator: true,
        headerToolbar: {
            left: '',
            center: 'title',
            right: ''
        },
        slotLabelFormat: {
            hour: 'numeric',
            minute: '2-digit',
            omitZeroMinute: true,
            meridiem: 'short'
        },
        slotMinTime: '07:00:00',
        slotMaxTime: '20:00:00',
        scrollTime: '07:00:00',
        editable: false,
        events: evenements
    });
    calendar.render();
});



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

// Ajouter un gestionnaire d'événement pour l'événement de redimensionnement de la fenêtre
window.addEventListener('resize', function() {
    // Réafficher les blocs en fonction de la largeur de la fenêtre
    showAllBlocks();
});

showAllBlocks();


var modal = document.getElementById("myPopup");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {

    // scroll to the top on the div whith the class f_posts
    var posts = document.getElementsByClassName("f_posts");
    for (var i = 0; i < posts.length; i++) {
        posts[i].scrollTop = 0;
    }

    modal.style.display = "block";
    // disable scroll in div with class f_posts 
    var posts = document.getElementsByClassName("f_posts");
    for (var i = 0; i < posts.length; i++) {
        posts[i].style.overflow = "hidden";
    }
    var boutton = document.getElementById("myBtn");
    boutton.style.display = "none";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
    // enable scroll in div with class f_posts
    var posts = document.getElementsByClassName("f_posts");
    for (var i = 0; i < posts.length; i++) {
        posts[i].style.overflow = "scroll";
    }
    var boutton = document.getElementById("myBtn");
    boutton.style.display = "block";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        // enable scroll in div with class f_posts
        var posts = document.getElementsByClassName("f_posts");
        for (var i = 0; i < posts.length; i++) {
            posts[i].style.overflow = "scroll";
        }
        var boutton = document.getElementById("myBtn");
        boutton.style.display = "block";
    }
}