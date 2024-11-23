// script that updates the text color of the <header> element to red (#FF0000)
document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('header');
    header.addEventListener('click', () => {
        header.classList.add('red');
    });
});
