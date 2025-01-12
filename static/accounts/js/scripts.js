
    document.addEventListener("DOMContentLoaded", function () {
    const passwordField = document.getElementById("password");
    const confirmPasswordField = document.getElementById("confirm_password");
    const passwordError = document.getElementById("password-error");
    const submitButton = document.getElementById("submit-btn");

    // Function to check if passwords match
    function checkPasswordMatch() {
        if (passwordField.value !== confirmPasswordField.value) {
            passwordError.style.display = "inline"; // Show error message
            submitButton.disabled = true; // Disable submit button
        } else {
            passwordError.style.display = "none"; // Hide error message
            submitButton.disabled = false; // Enable submit button
        }
    }

    // Event listeners for real-time password validation
    passwordField.addEventListener("input", checkPasswordMatch);
    confirmPasswordField.addEventListener("input", checkPasswordMatch);
    });