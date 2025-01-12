// Service Details Data
const serviceDetails = {
    carWash: {
      title: "Car Wash",
      description: "We provide top-notch car cleaning services to make your car shine like new. Choose from a range of services, including full detailing and interior cleaning."
    },
    maintenanceRepairs: {
      title: "Maintenance & Repairs",
      description: "Our expert team offers reliable maintenance and repair services, ensuring your car stays in excellent condition and safe on the road."
    },
    diagnosticsElectrical: {
      title: "Diagnostics & Electrical",
      description: "Using advanced diagnostic tools, we identify and fix electronic issues in your car, optimizing its performance and functionality."
    },
    accessoriesInstallation: {
      title: "Accessories Installation",
      description: "Upgrade your car with premium accessories, including sound systems, alarms, and custom installations tailored to your preferences."
    }
  };
  
  // Function to Show Modal with Service Details
  function showServiceDetails(serviceKey) {
    const modal = document.getElementById("serviceDetailsModal");
    const modalContent = document.getElementById("modalContent");
  
    if (serviceDetails[serviceKey]) {
      modalContent.innerHTML = `
        <h3>${serviceDetails[serviceKey].title}</h3>
        <p>${serviceDetails[serviceKey].description}</p>
      `;
      modal.style.display = "block";
    }
  }
  
  // Function to Close Modal
  function closeModal() {
    document.getElementById("serviceDetailsModal").style.display = "none";
  }
  
  // Close Modal on Outside Click
  window.onclick = function(event) {
    const modal = document.getElementById("serviceDetailsModal");
    if (event.target === modal) {
      modal.style.display = "none";
    }
  };
  