document.addEventListener("DOMContentLoaded", () => {
    const bookNowButtons = document.querySelectorAll(".book-now-btn");

    bookNowButtons.forEach((button) => {
        button.addEventListener("click", () => {
            // Trigger the form submission when the button is clicked
            button.closest("form").submit();  // Submitting the closest form
        });
    });
});
// Open confirmation modal
let cancelBookingId = null;

function confirmCancelBooking(bookingId) {
    cancelBookingId = bookingId;
    const modal = document.getElementById("confirmation-modal");
    modal.style.display = "block";
}

// Handle the 'Yes' confirmation
document.getElementById("confirm-btn").addEventListener("click", function() {
    if (cancelBookingId !== null) {
        // Submit the cancellation form
        document.getElementById("cancel-booking-form-" + cancelBookingId).submit();
    }
    const modal = document.getElementById("confirmation-modal");
    modal.style.display = "none";
});

// Handle the 'No' cancellation
document.getElementById("cancel-btn").addEventListener("click", function() {
    const modal = document.getElementById("confirmation-modal");
    modal.style.display = "none";
});

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById("confirmation-modal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

document.addEventListener("DOMContentLoaded", () => {
    const cancelButtons = document.querySelectorAll(".cancel-booking-btn");

    cancelButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            const bookingId = button.getAttribute("data-booking-id");
            const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value; // Fetch CSRF token

            // Show confirmation modal
            const confirmModal = confirm("Are you sure you want to cancel this booking?");
            if (confirmModal) {
                fetch(`/booking/cancel-booking/${bookingId}/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfToken,  // Include CSRF token
                    },
                })
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.error) {
                            // If booking can't be canceled, show error modal with message
                            document.getElementById('cancelErrorMessage').innerText = data.error;
                            document.getElementById('cancelErrorModal').style.display = 'block';
                        } else {
                            // Redirect to dashboard after successful cancellation
                            window.location.href = '/dashboard';  // Redirect to the dashboard
                        }
                    })
                    .catch((error) => console.error("Error:", error));
            }
        });
    });
});

// Function to close the error modal
function closeModal() {
    document.getElementById('cancelErrorModal').style.display = 'none';
}

