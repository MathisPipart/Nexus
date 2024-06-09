document.addEventListener('DOMContentLoaded', function() {
        const calendarEl = document.getElementById('calendar');
        let calendar = new FullCalendar.Calendar(calendarEl, {
        timeZone: 'europe/Paris',
        initialView: 'timeGridWeek',
        height: 'auto',
        locale: 'fr',
        hiddenDays: [ 0 ], // Masquer les dimanches
        nowIndicator: true, // Afficher la ligne actuelle
        headerToolbar: {
            left: 'prev,next,today',
            center: 'title',
            right: 'timeGridWeek,dayGridMonth'
        },
        slotLabelFormat: {
            hour: 'numeric',
            minute: '2-digit',
            omitZeroMinute: true,
            meridiem: 'short'
        },
        slotMinTime: '07:00:00', // Heure de début de la grille de temps
        slotMaxTime: '20:00:00', // Heure de fin de la grille de temps
        scrollTime: '07:00:00', // Définir le défilement initial à 7h du matin
        editable: false,
        events: evenements
    });
calendar.render();
});