document.addEventListener('DOMContentLoaded', function() {
    // FOLLOW BUTTONS A
    var followButtonsA = document.querySelectorAll('.follow-btnA');
  
    followButtonsA.forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.stopPropagation();
        event.preventDefault();
      });

      button.addEventListener('mousedown', function(event) {
        this.closest('.club-cardA').classList.add('prevent-active-style');
      });
      button.addEventListener('mouseup', function(event) {
        setTimeout(() => {
          this.closest('.club-cardA').classList.remove('prevent-active-style');
        }, 0);
      });
    });

    document.getElementById('followBtn').addEventListener('click', function() {
        var currentValue = this.value;
        var numberPattern = /\d+/g;
        var currentFollowers = parseInt(currentValue.match(numberPattern), 10);
        
        currentFollowers++;
        
        // Mise à jour de la valeur du bouton avec le nouveau nombre d'abonnés
        this.value = currentFollowers + ' abonnés';
    });

    // FOLLOW BUTTONS B
    var followButtonsB = document.querySelectorAll('.follow-btnB');
  
    followButtonsB.forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.stopPropagation();
        event.preventDefault();
      });

      button.addEventListener('mousedown', function(event) {
        this.closest('.club-cardB').classList.add('prevent-active-style');
      });
      button.addEventListener('mouseup', function(event) {
        setTimeout(() => {
          this.closest('.club-cardB').classList.remove('prevent-active-style');
        }, 0);
      });
    });


    // CONVERSATION BUTTONS A
    var convButtonsA = document.querySelectorAll('.conv-btnA');

    convButtonsA.forEach(function(button) {
        button.addEventListener('click', function(event) {
        event.stopPropagation();
        event.preventDefault();
        });

        button.addEventListener('mousedown', function(event) {
        this.closest('.club-cardA').classList.add('prevent-active-style');
        });
        button.addEventListener('mouseup', function(event) {
        setTimeout(() => {
            this.closest('.club-cardA').classList.remove('prevent-active-style');
        }, 0);
        });
    });

    // CONVERSATION BUTTONS B
    var convButtonsB = document.querySelectorAll('.conv-btnB');
    
    convButtonsB.forEach(function(button) {
        button.addEventListener('click', function(event) {
        event.stopPropagation();
        event.preventDefault();
        });

        button.addEventListener('mousedown', function(event) {
        this.closest('.club-cardB').classList.add('prevent-active-style');
        });
        button.addEventListener('mouseup', function(event) {
        setTimeout(() => {
            this.closest('.club-cardB').classList.remove('prevent-active-style');
        }, 0);
        });
    });
  });
  