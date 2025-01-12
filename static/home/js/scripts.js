document.addEventListener('DOMContentLoaded', () => {
    console.log('Interactive Testimonials and Features Loaded');
    // Example: Animate testimonials on hover (if needed in the future)
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    testimonialCards.forEach(card => {
        card.addEventListener('mouseover', () => {
            card.style.transform = 'scale(1.02)';
        });
        card.addEventListener('mouseout', () => {
            card.style.transform = 'scale(1)';
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    console.log('Pricing Overview Section Loaded');
    
    // Example dynamic functionality: Show an alert on clicking a price (future dynamic pricing feature)
    const priceItems = document.querySelectorAll('.price-item');
    priceItems.forEach(item => {
        item.addEventListener('click', () => {
            alert(`You clicked on ${item.firstChild.textContent.trim()}`);
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const ctaButton = document.querySelector('.cta-banner .btn-primary');
    
    ctaButton.addEventListener('click', () => {
        console.log('CTA Button Clicked: Redirecting to Booking Page');
    });
});

// Simple form validation for the signup page
document.querySelector('.signup-form').addEventListener('submit', function(e) {
    const password = document.getElementById('password').value;
    const passwordConfirm = document.getElementById('password_confirm').value;

    if (password !== passwordConfirm) {
        e.preventDefault();
        alert('Passwords do not match!');
    }
});
