document.addEventListener('DOMContentLoaded', function() {
    // Gestion du clic sur le triangle pour les étudiants
    var toggleEtudiant = document.querySelector('.triangleEtudiant');
    if (toggleEtudiant) {
        toggleEtudiant.addEventListener('click', function(e) {
            e.preventDefault();
            var rankingSectionEtudiant = document.querySelector('.classement_Etudiant');
            rankingSectionEtudiant.classList.toggle('visible');
            this.querySelector('img').classList.toggle('rotate-180');
        });
    }

    // Gestion du clic sur le triangle pour les clubs
    var toggleClub = document.querySelector('.triangleClub');
    if (toggleClub) {
        toggleClub.addEventListener('click', function(e) {
            e.preventDefault();
            var rankingSectionClub = document.querySelector('.classement_Club');
            rankingSectionClub.classList.toggle('visible');
            this.querySelector('img').classList.toggle('rotate-180');
        });
    }
});
