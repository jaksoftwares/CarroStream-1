// Show the Add Service form
document.getElementById("add-service-btn").addEventListener("click", function() {
    var addServiceForm = document.getElementById("add-service-form");
    addServiceForm.style.display = "block"; // Show the form

    // Disable background scrolling
    document.body.style.overflow = "hidden";
});

// Hide the Add Service form
document.getElementById("close-service-form-btn").addEventListener("click", function() {
    var addServiceForm = document.getElementById("add-service-form");
    addServiceForm.style.display = "none"; // Hide the form

    // Enable background scrolling again
    document.body.style.overflow = "auto";
});


// Delete a service
function deleteService(serviceId) {
    // Get CSRF token value from the hidden input field
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send the delete request to the backend
    fetch(`/services/delete-service/${serviceId}/`, {
        method: 'POST',  // Use 'POST' for deletion, as per Django's convention
        headers: {
            'Content-Type': 'application/json',  // Specify content type as JSON
            'X-CSRFToken': csrfToken,  // Add CSRF token to the request headers
        },
        body: JSON.stringify({ service_id: serviceId })  // Send service ID in the body
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Remove the service row from the table if the deletion was successful
            const row = document.getElementById(`service-${serviceId}`);
            row.remove();
        } else {
            alert("Failed to delete the service: " + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error deleting the service.");
    });
}
