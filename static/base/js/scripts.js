let isScrolling; // Tracks scrolling activity
  const navbar = document.querySelector('header.navbar');

  // Show navbar when scrolling stops
  const showNavbar = () => {
    navbar.classList.add('visible');
  };

  // Hide navbar during scrolling
  const hideNavbar = () => {
    navbar.classList.remove('visible');
  };

  window.addEventListener('scroll', () => {
    // Clear the timeout whenever a scroll event is fired
    clearTimeout(isScrolling);

    // Hide the navbar while scrolling
    hideNavbar();

    // Set a timeout to show the navbar when scrolling stops
    isScrolling = setTimeout(showNavbar, 200); // Adjust delay as needed
  });

  // Ensure the navbar is visible initially
  showNavbar();