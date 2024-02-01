// Self Quiz calls this function whenever the show back side button is clicked
function showBackSide() {
    var answer = document.getElementById('back')
    var showButton = document.getElementById('show_back')
    var displaySetting = back.style.display;

    // Reveals the back side of the flashcard when button is clicked
    if(displaySetting == 'block') {
        back.style.display = 'none';
        showButton.innerHTML = 'Show Back Side';
    } else {
        back.style.display = 'block';
        showButton.innerHTML = 'Hide Back Side';
    }
}


