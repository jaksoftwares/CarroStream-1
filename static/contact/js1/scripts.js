// Basic form validation (Optional)
document.querySelector('form').addEventListener('submit', function(e) {
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;

    if (!name || !email || !message) {
        e.preventDefault();
        alert('Please fill in all fields before submitting.');
    }
});
