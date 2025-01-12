function openNewsletterModal() {
    document.getElementById('newsletter-modal').style.display = 'flex';
}

function closeNewsletterModal() {
    document.getElementById('newsletter-modal').style.display = 'none';
}

function openNotificationsModal() {
    document.getElementById('notifications-modal').style.display = 'flex';
}

function closeNotificationsModal() {
    document.getElementById('notifications-modal').style.display = 'none';
}

// Show specific user input for notifications
document.getElementById('recipients').addEventListener('change', function() {
    const specificUsers = document.getElementById('specific-users');
    if (this.value === 'specific') {
        specificUsers.style.display = 'block';
    } else {
        specificUsers.style.display = 'none';
    }
});
