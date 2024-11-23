// Wait for the DOM to load before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Select the target elements
    const addItem = document.getElementById('add_item');
    const removeItem = document.getElementById('remove_item');
    const clearList = document.getElementById('clear_list');
    const myList = document.querySelector('.my_list');

    // Event listener for adding a new <li> element
    addItem.addEventListener('click', () => {
        const newListItem = document.createElement('li');
        newListItem.textContent = 'Item';
        myList.appendChild(newListItem);
    });

    // Event listener for removing the last <li> element
    removeItem.addEventListener('click', () => {
        if (myList.lastElementChild) {
            myList.removeChild(myList.lastElementChild);
        }
    });

    // Event listener for clearing all <li> elements
    clearList.addEventListener('click', () => {
        myList.innerHTML = '';
    });
});
