// Form Submission Handler
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('.contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Show loading state
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            submitButton.textContent = 'Sending...';
            submitButton.disabled = true;
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
