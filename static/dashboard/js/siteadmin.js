// JavaScript for CRUD operations

document.getElementById("add-service-btn").onclick = function() {
    document.getElementById("service-form").style.display = "block";
    document.getElementById("form-title").textContent = "Add Service";
    document.getElementById("service-id").value = "";
    document.getElementById("service-form-content").reset();
};

document.getElementById("service-form-content").onsubmit = function(event) {
    event.preventDefault();
    const serviceId = document.getElementById("service-id").value;
    const url = serviceId ? `/services/edit/${serviceId}/` : '/services/add/';
    const formData = new FormData(document.getElementById("service-form-content"));
    
    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Show success popup
            showSuccessPopup(data.message);
            
            // Dynamically add the new service to the table
            const newService = data.service;  // Assuming the response contains the new service data
            const newRow = document.createElement("tr");
            newRow.id = `service-${newService.id}`;
            newRow.innerHTML = `
                <td>${newService.title}</td>
                <td>${newService.price}</td>
                <td>${newService.image}</td>
                <td>
                    <button onclick="editService(${newService.id})">Edit</button>
                    <button onclick="deleteService(${newService.id})">Delete</button>
                </td>
            `;
            document.querySelector("#services-table tbody").appendChild(newRow);
            
            // Hide the form after successful submission
            document.getElementById("service-form").style.display = "none";
        }
    });
};

// Show success popup
function showSuccessPopup(message) {
    const popup = document.createElement("div");
    popup.classList.add("success-popup");
    popup.textContent = message;
    document.body.appendChild(popup);

    // Set a timeout to remove the popup after 3 seconds
    setTimeout(() => {
        popup.remove();
    }, 3000);  // 3000 milliseconds = 3 seconds
}

// Handle form submission (Add/Edit)
document.getElementById("service-form-content").onsubmit = function(event) {
    event.preventDefault();
    const serviceId = document.getElementById("service-id").value;
    const url = serviceId ? `/services/edit/${serviceId}/` : '/services/add/';
    const formData = new FormData(document.getElementById("service-form-content"));

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Hide the form
            document.getElementById("service-form").style.display = "none";

            // Show the success popup
            showSuccessPopup(data.message);

            // Update the services table dynamically
            updateServicesTable(data.services);
        }
    });
};

// Function to update the services table dynamically
function updateServicesTable(services) {
    const tableBody = document.getElementById("services-table").getElementsByTagName("tbody")[0];
    tableBody.innerHTML = "";  // Clear the table

    // Add each service to the table
    services.forEach(service => {
        const row = tableBody.insertRow();
        row.id = `service-${service.id}`;

        const titleCell = row.insertCell(0);
        titleCell.textContent = service.title;

        const priceCell = row.insertCell(1);
        priceCell.textContent = service.price;

        const actionsCell = row.insertCell(2);
        actionsCell.innerHTML = `
            <button onclick="editService(${service.id})">Edit</button>
            <button onclick="deleteService(${service.id})">Delete</button>
        `;
    });
}

// Show the form to add a new service
document.getElementById("add-service-btn").onclick = function() {
    document.getElementById("service-form").style.display = "block";
    document.getElementById("form-title").textContent = "Add Service";
    document.getElementById("service-id").value = "";
    document.getElementById("service-form-content").reset();
};

// JavaScript to edit the service
function editService(serviceId) {
    // Fetch existing service data to pre-fill the form
    fetch(`/services/edit/${serviceId}/`)
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Pre-fill the form with the service data
            document.getElementById("edit-service-form").style.display = "block";
            document.getElementById("service-id").value = data.service.id;
            document.getElementById("edit-title").value = data.service.title;
            document.getElementById("edit-price").value = data.service.price;
            document.getElementById("edit-description").value = data.service.description;
            // Image field can be handled if needed, but for simplicity, we assume it is updated manually.
        } else {
            alert('Failed to fetch service details');
        }
    });
}

// JavaScript to handle the form submission (Save the changes)
document.getElementById("edit-service-form-content").onsubmit = function(event) {
    event.preventDefault();
    
    const serviceId = document.getElementById("service-id").value;
    const url = `/services/edit/${serviceId}/`; // URL to update the service
    
    // Get form data
    const formData = new FormData(document.getElementById("edit-service-form-content"));
    
    // Send the data to the backend to update the service
    fetch(url, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Update the UI to reflect the updated service
            updateServiceInTable(data.service);
            
            // Show success message
            alert(data.message);
            
            // Hide the edit form after successful update
            document.getElementById("edit-service-form").style.display = "none";
        } else {
            // If there's an error, alert the user
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error saving service:', error);
        alert('Error saving service');
    });
};

// Function to update the service in the table
function updateServiceInTable(updatedService) {
    const serviceRow = document.getElementById(`service-${updatedService.id}`);
    if (serviceRow) {
        serviceRow.querySelector('td:nth-child(1)').textContent = updatedService.title;
        serviceRow.querySelector('td:nth-child(2)').textContent = updatedService.price;
    }
}


// Handle form submission (Add/Edit)
document.getElementById("service-form-content").onsubmit = function(event) {
    event.preventDefault();

    const serviceId = document.getElementById("service-id").value;
    const url =`/services/add/${serviceId}/`;
    const formData = new FormData(document.getElementById("service-form-content"));

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Show success popup
            showSuccessPopup(data.message);
            
            // Dynamically update the services table (reload the service list)
            updateServicesTable(data.services);

            // Hide the form after successful submission
            document.getElementById("service-form").style.display = "none";
        } else {
            alert("Error updating service.");
        }
    });
};

function deleteService(serviceId) {
    if (confirm("Are you sure you want to delete this service?")) {
        fetch(`/services/delete/${serviceId}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCSRFToken() // Include CSRF token
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert(data.message);

                // Remove the deleted service row from the table
                const row = document.getElementById(`service-${serviceId}`);
                row.remove();
            } else {
                alert("Error: " + data.message);
            }
        });
    }
}

// Function to get the CSRF token (required for Django)
function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return '';
}
