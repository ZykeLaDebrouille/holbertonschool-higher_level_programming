// Wait for the DOM to load before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Select elements
    const translateButton = document.getElementById('btn_translate');
    const languageCode = document.getElementById('language_code');
    const helloDiv = document.getElementById('hello');

    // Event listener for the "Translate" button
    translateButton.addEventListener('click', () => {
        const lang = languageCode.value; // Get selected language code
        if (lang) {
            // Fetch translation from the API
            fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Display the translated "Hello" in the helloDiv
                    helloDiv.textContent = data.hello;
                })
                .catch(error => {
                    // Log any errors to the console
                    console.error('There was a problem with the fetch operation:', error);
                    helloDiv.textContent = 'Error fetching translation';
                });
        } else {
            // If no language is selected, display a message
            helloDiv.textContent = 'Please select a language.';
        }
    });
});
