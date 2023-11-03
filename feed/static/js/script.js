//alert("Max la saucisse");

//print test in cosol
console.log("Max la saucisse");

$(document).ready(function() {
    // Gestion du clic sur un élément de la liste déroulante
    $('.dropdown-item').click(function() {
        // Masquez tous les blocs de contenu
        $('.f_posts, .f_conversations').hide();

        // Récupérez l'identifiant du bloc de contenu cible à partir de l'attribut 'data-target'
        var target = $(this).data('target');

        // Affichez le bloc de contenu cible
        $('#' + target).show();

        // Log the text of the clicked item
        var itemText = $(this).text();
        console.log("Clicked item: " + itemText);
    });
});
