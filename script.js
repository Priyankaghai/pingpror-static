// Form Submission Handler
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('.contact-form');
    const heroForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Show loading state
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            submitButton.textContent = 'Sending...';
            submitButton.disabled = true;
        });
    }

    // Hero Form Validation
    if (heroForm) {
        heroForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form elements
            const termsCheckbox = document.getElementById('terms_conditions');
            const recaptchaResponse = grecaptcha.getResponse();
            const submitBtn = document.getElementById('submitBtn');
            
            // Clear previous error messages
            clearErrorMessages();
            
            // Validate Terms and Conditions
            if (!termsCheckbox.checked) {
                showError('terms_conditions', 'Please accept the Terms of Use and Privacy Policy to continue.');
                return false;
            }
            
            // Validate reCAPTCHA
            if (!recaptchaResponse) {
                showError('recaptcha', 'Please complete the reCAPTCHA verification.');
                return false;
            }
            
            // If validation passes, submit the form
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;
            
            // Add reCAPTCHA response to form
            const recaptchaInput = document.createElement('input');
            recaptchaInput.type = 'hidden';
            recaptchaInput.name = 'g-recaptcha-response';
            recaptchaInput.value = recaptchaResponse;
            this.appendChild(recaptchaInput);
            
            // Submit the form
            this.submit();
        });
    }
    
    // Function to show error messages
    function showError(fieldId, message) {
        let errorElement = document.getElementById(fieldId + '_error');
        if (!errorElement) {
            errorElement = document.createElement('div');
            errorElement.id = fieldId + '_error';
            errorElement.className = 'error-message';
            
            const field = document.getElementById(fieldId);
            if (field) {
                field.parentNode.appendChild(errorElement);
            }
        }
        errorElement.textContent = message;
        errorElement.classList.add('show');
    }
    
    // Function to clear error messages
    function clearErrorMessages() {
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(error => {
            error.classList.remove('show');
        });
    }

    // Array of client objects
    const clients = [
        { name: "APAC", img: "clients/apac.png" },
        { name: "Max Life", img: "clients/maxlife.png" },
        { name: "Ciena", img: "clients/ciena.png" },
        { name: "Rajdarbar Realty", img: "clients/rajdarbar.png" },
        { name: "Chokhi Dhani", img: "clients/chokhidhani.png" },
        { name: "Domino", img: "clients/domino.png" },
        { name: "OAP", img: "clients/oap.png" },
        { name: "Vishwam Ayurveda", img: "clients/vishwam.png" },
        { name: "Idealspaze", img: "clients/idealspaze.png" },
        { name: "Atulyam", img: "clients/atulyam.png" },
        { name: "CocaCola", img: "clients/cocacola.png" },
        { name: "Rajshila", img: "clients/rajshila.png" },
        { name: "Counterpoint", img: "clients/counterpoint.png" },
        { name: "Sabrangi", img: "clients/sabrangi.png" },
        { name: "The Bamboo Co", img: "clients/bamboo.png" }
    ];

    const clientsContainer = document.getElementById('clients-logos');
    if (clientsContainer) {
        clients.forEach(client => {
            const img = document.createElement('img');
            img.src = client.img;
            img.alt = client.name;
            clientsContainer.appendChild(img);
        });
    }
});
