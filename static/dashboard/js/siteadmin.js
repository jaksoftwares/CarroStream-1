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
// Show the Add team form
document.getElementById("add-team-btn").addEventListener("click", function() {
    var addTeamForm = document.getElementById("team-form");
    addTeamForm.style.display = "block"; // Show the form

    // Disable background scrolling
    document.body.style.overflow = "hidden";
});
// Hide the Add Service form
document.getElementById("close-team-form-btn").addEventListener("click", function() {
    var addTeamForm = document.getElementById("team-form");
    addTeamForm.style.display = "none"; // Hide the form

    // Enable background scrolling again
    document.body.style.overflow = "auto";
});

function editService(serviceId) {
    // Show the form
    document.getElementById('add-service-form').style.display = 'block';
    document.getElementById('form-title').textContent = 'Edit Service';
    
    // Get the service data from the table row
    const row = document.getElementById(`service-${serviceId}`);
    const title = row.querySelector('td:nth-child(1)').textContent;
    const price = row.querySelector('td:nth-child(2)').textContent;
    const description = row.querySelector('td:nth-child(3)').textContent;

    // Populate the form with the existing data
    document.getElementById('title').value = title;
    document.getElementById('price').value = price;
    document.getElementById('description').value = description;
    document.getElementById('image').value = '';  // Reset image input (for file upload)
    document.getElementById('service-id').value = serviceId;

    // Update the form action to point to the correct edit URL in the services app
    const form = document.getElementById('service-form-content');
    form.action = '/services/edit/' + serviceId + '/';  // Adjusting the URL to edit service within the services app
}


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


// Show the Add Team form
document.getElementById("add-team-btn").addEventListener("click", function () {
    var addTeamForm = document.getElementById("team-form");
    addTeamForm.style.display = "block"; // Show the form
    document.body.style.overflow = "hidden"; // Disable background scrolling
});

// Hide the Add Team form
document.getElementById("close-team-form-btn").addEventListener("click", function () {
    var addTeamForm = document.getElementById("team-form");
    addTeamForm.style.display = "none"; // Hide the form
    document.body.style.overflow = "auto"; // Enable background scrolling
});

function editTeam(teamId) {
    // Show the form
    document.getElementById('team-form').style.display = 'block';

    // Get the team data from the table row
    const row = document.getElementById(`team-${teamId}`);
    const name = row.querySelector('td:nth-child(1)').textContent.trim();
    const role = row.querySelector('td:nth-child(2)').textContent.trim();

    // Populate the form with existing data
    document.getElementById('name').value = name; // Ensure IDs match the form
    document.getElementById('role').value = role;
    document.getElementById('team-id').value = teamId;

    // Update the form action to the correct edit URL
    const form = document.getElementById('team-form-content');
    form.action = `/team/edit/${teamId}/`; // Adjust the URL to your backend route
}

function deleteTeam(teamId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(`/team/delete-team/${teamId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ team_id: teamId })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const row = document.getElementById(`team-${teamId}`);
                row.remove(); // Remove the team member from the table
            } else {
                alert("Failed to delete the team member: " + (data.error || 'Unknown error'));
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Error deleting the team member.");
        });
}


// Show the Add Testimonial form
document.getElementById("add-testimonial-btn").addEventListener("click", function() {
    var addTestimonialForm = document.getElementById("testimonial-form");
    addTestimonialForm.style.display = "block"; // Show the form

    // Disable background scrolling
    document.body.style.overflow = "hidden";
});

// Hide the Add Testimonial form
document.getElementById("close-testimonial-form-btn").addEventListener("click", function() {
    var addTestimonialForm = document.getElementById("testimonial-form");
    addTestimonialForm.style.display = "none"; // Hide the form

    // Enable background scrolling again
    document.body.style.overflow = "auto";
});

function editTestimonial(testimonialId) {
    document.getElementById('testimonial-form').style.display = 'block';
    
    const row = document.getElementById(`testimonial-${testimonialId}`);
    const user = row.querySelector('td:nth-child(1)').textContent;
    const feedback = row.querySelector('td:nth-child(2)').textContent;

    document.getElementById('testimonial-user').value = user;
    document.getElementById('testimonial-feedback').value = feedback;
    document.getElementById('testimonial-id').value = testimonialId;

    const form = document.getElementById('testimonial-form-content');
    form.action = '/testimonials/edit/' + testimonialId + '/';
}

function deleteTestimonial(testimonialId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch(`/testimonials/delete-testimonial/${testimonialId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ testimonial_id: testimonialId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const row = document.getElementById(`testimonial-${testimonialId}`);
            row.remove();
        } else {
            alert("Failed to delete the testimonial: " + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error deleting the testimonial.");
    });
}



// Show the Add FAQ form
document.getElementById("add-faq-btn").addEventListener("click", function() {
    var addFaqForm = document.getElementById("faq-form");
    addFaqForm.style.display = "block"; // Show the form

    document.body.style.overflow = "hidden";
});

// Hide the Add FAQ form
document.getElementById("close-faq-form-btn").addEventListener("click", function() {
    var addFaqForm = document.getElementById("faq-form");
    addFaqForm.style.display = "none"; // Hide the form

    document.body.style.overflow = "auto";
});

function editFaq(faqId) {
    document.getElementById('faq-form').style.display = 'block';
    
    const row = document.getElementById(`faq-${faqId}`);
    const question = row.querySelector('td:nth-child(1)').textContent;
    const answer = row.querySelector('td:nth-child(2)').textContent;

    document.getElementById('faq-question').value = question;
    document.getElementById('faq-answer').value = answer;
    document.getElementById('faq-id').value = faqId;

    const form = document.getElementById('faq-form-content');
    form.action = '/faqs/edit/' + faqId + '/';
}

function deleteFaq(faqId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch(`/faqs/delete-faq/${faqId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ faq_id: faqId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const row = document.getElementById(`faq-${faqId}`);
            row.remove();
        } else {
            alert("Failed to delete the FAQ: " + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error deleting the FAQ.");
    });
}


// Show the Add Booking form
document.getElementById("add-booking-btn").addEventListener("click", function() {
    var addBookingForm = document.getElementById("booking-form");
    addBookingForm.style.display = "block"; // Show the form

    document.body.style.overflow = "hidden";
});

// Hide the Add Booking form
document.getElementById("close-booking-form-btn").addEventListener("click", function() {
    var addBookingForm = document.getElementById("booking-form");
    addBookingForm.style.display = "none"; // Hide the form

    document.body.style.overflow = "auto";
});

function editBooking(bookingId) {
    document.getElementById('booking-form').style.display = 'block';
    
    const row = document.getElementById(`booking-${bookingId}`);
    const user = row.querySelector('td:nth-child(1)').textContent;
    const service = row.querySelector('td:nth-child(2)').textContent;
    const date = row.querySelector('td:nth-child(3)').textContent;
    const status = row.querySelector('td:nth-child(4)').textContent;

    document.getElementById('booking-user').value = user;
    document.getElementById('booking-service').value = service;
    document.getElementById('booking-date').value = date;
    document.getElementById('booking-status').value = status;
    document.getElementById('booking-id').value = bookingId;

    const form = document.getElementById('booking-form-content');
    form.action = '/bookings/edit/' + bookingId + '/';
}

function deleteBooking(bookingId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch(`/bookings/delete-booking/${bookingId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ booking_id: bookingId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const row = document.getElementById(`booking-${bookingId}`);
            row.remove();
        } else {
            alert("Failed to delete the booking: " + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error deleting the booking.");
    });
}


// Show the Add Payment form
document.getElementById("add-payment-btn").addEventListener("click", function() {
    var addPaymentForm = document.getElementById("payment-form");
    addPaymentForm.style.display = "block"; // Show the form

    document.body.style.overflow = "hidden";
});

// Hide the Add Payment form
document.getElementById("close-payment-form-btn").addEventListener("click", function() {
    var addPaymentForm = document.getElementById("payment-form");
    addPaymentForm.style.display = "none"; // Hide the form

    document.body.style.overflow = "auto";
});

function viewPayment(paymentId) {
    // You can display the payment details in a modal or section
    alert("Viewing payment details for payment ID: " + paymentId);
}

function deletePayment(paymentId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch(`/payments/delete-payment/${paymentId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ payment_id: paymentId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const row = document.getElementById(`payment-${paymentId}`);
            row.remove();
        } else {
            alert("Failed to delete the payment: " + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error deleting the payment.");
    });
}


// Updating the booking status

function updateStatus(bookingId) {
    const newStatus = document.getElementById(`status-${bookingId}`).value;

    fetch(`/update-booking-status/${bookingId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ status: newStatus }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(`Booking status updated to ${newStatus}`);
        } else {
            alert('Failed to update booking status. Please try again.');
        }
    });
}

// CSRF Token Helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Profile section edit functionality
document.addEventListener('DOMContentLoaded', () => {
    const editProfileBtn = document.getElementById('edit-profile-btn');
    const cancelEditBtn = document.getElementById('cancel-edit-btn');
    const profileDetails = document.getElementById('profile-details');
    const editProfileForm = document.getElementById('edit-profile-form');

    editProfileBtn.addEventListener('click', () => {
        profileDetails.style.display = 'none';
        editProfileForm.style.display = 'block';
    });

    cancelEditBtn.addEventListener('click', () => {
        editProfileForm.style.display = 'none';
        profileDetails.style.display = 'block';
    });
});
