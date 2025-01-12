// Search FAQ Functionality
function searchFAQ() {
    const query = document.getElementById('search-faq').value.toLowerCase();
    const faqs = document.querySelectorAll('.card');

    faqs.forEach(function(faq) {
        const question = faq.querySelector('.btn-link').textContent.toLowerCase();
        
        if (question.indexOf(query) !== -1) {
            faq.style.display = '';
        } else {
            faq.style.display = 'none';
        }
    });
}
