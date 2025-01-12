document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("paymentModal");
    const successModal = document.getElementById("successModal");
    const openModalBtn = document.getElementById("openModalBtn");
    const closeModalBtn = document.getElementById("closeModalBtn");
    const closeSuccessModalBtn = document.getElementById("closeSuccessModalBtn");

    // Open Payment Modal
    openModalBtn.addEventListener("click", () => {
        modal.style.display = "block";
    });

    // Close Payment Modal
    closeModalBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Close Success Modal
    closeSuccessModalBtn.addEventListener("click", () => {
        successModal.style.display = "none";
    });

    // Close Modal When Clicking Outside
    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
        if (event.target === successModal) {
            successModal.style.display = "none";
        }
    });

    // Show the success modal after payment processing
    const showSuccessModal = () => {
        modal.style.display = "none";  // Close payment modal
        successModal.style.display = "block";  // Show success modal
    };

    // Attach showSuccessModal to the global scope for success after form submission
    window.showSuccessModal = showSuccessModal;
});


 // Get the modal element and the button that triggers it
var modal = document.getElementById("bookingModal");
var openModalBtn = document.querySelector(".book-service-btn");  // Adjusted to use your class
var closeModalBtn = document.querySelector(".close-btn");

// When the "Book New Service" button is clicked, open the modal
openModalBtn.addEventListener("click", function(event) {
    var serviceId = openModalBtn.getAttribute("data-service-id");  // Get the service ID from the button's data attribute
    var serviceSelect = document.querySelector("#service");  // Get the service dropdown

    // Set the service ID in the dropdown
    serviceSelect.value = serviceId;

    modal.style.display = "block";  // Show the modal
});

// When the user clicks the close button, close the modal
closeModalBtn.addEventListener("click", function() {
    modal.style.display = "none";  // Hide the modal
});

// When the user clicks outside the modal, close it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";  // Hide the modal
    }
};