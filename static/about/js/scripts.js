// Select the carousel container and slides
const slides = document.querySelectorAll('.carousel-slide');
let currentIndex = 0;

// Function to show the next slide
function showNextSlide() {
  // Remove 'active' class from current slide
  slides[currentIndex].classList.remove('active');

  // Increment index (wrap around to 0 if at the last slide)
  currentIndex = (currentIndex + 1) % slides.length;

  // Add 'active' class to the next slide
  slides[currentIndex].classList.add('active');
}

// Set the interval to change slides every 3 seconds (3000 milliseconds)
setInterval(showNextSlide, 10000);  // Adjust the timing as needed
