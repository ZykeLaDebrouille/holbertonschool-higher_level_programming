// script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header
document.getElementById('red_header').addEventListener('click', () => {
    document.querySelector('header').style.color = '#FF0000'; // Change la couleur de l'en-tête en rouge lors du clic
});
