if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/static/js/service-worker.js')
            .then(registration => {
            })
            .catch(err => {
            });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.getElementById('primary-navigation');
    const nav = document.querySelector('nav');
    
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function() {
            const isOpen = hamburger.classList.toggle('open');
            navLinks.classList.toggle('open');
            if (nav) nav.classList.toggle('open');
            hamburger.setAttribute('aria-expanded', isOpen);
        });
        
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                hamburger.classList.remove('open');
                navLinks.classList.remove('open');
                if (nav) nav.classList.remove('open');
                hamburger.setAttribute('aria-expanded', 'false');
            });
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                const target = document.querySelector(href);
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
    
    if ('IntersectionObserver' in window) {
        const lazyImages = document.querySelectorAll('img[loading="lazy"]');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.src || img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        lazyImages.forEach(img => observer.observe(img));
    }
});

document.addEventListener('load', function(e) {
    if (e.target.tagName === 'IMG') {
        e.target.classList.add('loaded');
    }
}, true);

window.preselectService = function(serviceTitle, event) {
    if (event) {
        event.preventDefault();
    }
    
    const contactSection = document.getElementById('contact');
    if (!contactSection) return;
    
    contactSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    
    const serviceSelect = document.getElementById('id_service_type');
    if (serviceSelect) {
        let matchedValue = "";
        const cleanedTitle = serviceTitle.toLowerCase().trim();
        
        for (let i = 0; i < serviceSelect.options.length; i++) {
            const option = serviceSelect.options[i];
            const optionValue = option.value.toLowerCase().trim();
            const optionText = option.text.toLowerCase().trim();
            
            if (optionValue !== "" && (
                cleanedTitle.includes(optionValue) || 
                optionValue.includes(cleanedTitle) ||
                cleanedTitle.includes(optionText) || 
                optionText.includes(cleanedTitle)
            )) {
                matchedValue = option.value;
                break;
            }
        }
        
        if (matchedValue) {
            serviceSelect.value = matchedValue;
            
            const changeEvent = new Event('change', { bubbles: true });
            serviceSelect.dispatchEvent(changeEvent);
            
            serviceSelect.classList.remove('glow-highlight');
            void serviceSelect.offsetWidth;
            serviceSelect.classList.add('glow-highlight');
            
            setTimeout(() => {
                serviceSelect.classList.remove('glow-highlight');
            }, 2600);
        }
    }
    
    const nameField = document.getElementById('id_name');
    if (nameField) {
        setTimeout(() => {
            nameField.focus({ preventScroll: true });
        }, 800);
    }
};

document.addEventListener('DOMContentLoaded', function() {
    const serviceSelect = document.getElementById('id_service_type');
    const serviceTip = document.getElementById('service-tip');
    const phoneInput = document.getElementById('id_phone');
    const phoneMsg = document.getElementById('phone-validation-msg');

    const serviceHints = {
        'LOCAL': 'Local bookings include 80km / 8hr usage. Extra km/hr charges apply.',
        'OUTSTATION': 'Outstation bookings have a minimum 250km/day billing.',
        'AIRPORT': 'Airport transfers include toll & parking charges.'
    };

    if (serviceSelect && serviceTip) {
        serviceSelect.addEventListener('change', function() {
            const val = this.value;
            if (serviceHints[val]) {
                serviceTip.textContent = serviceHints[val];
                serviceTip.style.opacity = '1';
            } else {
                serviceTip.style.opacity = '0';
                setTimeout(() => serviceTip.textContent = '', 300);
            }
        });
        
        if (serviceSelect.value) {
            serviceSelect.dispatchEvent(new Event('change'));
        }
    }

    if (phoneInput && phoneMsg) {
        phoneInput.addEventListener('input', function() {
            const val = this.value.replace(/\D/g, '');
            if (val.length > 0 && val.length < 10) {
                phoneMsg.textContent = 'Please enter a valid 10-digit number';
                phoneMsg.style.color = 'var(--orange)';
            } else if (val.length >= 10) {
                phoneMsg.textContent = '✓ Valid number format';
                phoneMsg.style.color = '#10B981';
            } else {
                phoneMsg.textContent = '';
            }
        });
    }

    const starContainer = document.getElementById('star-rating-container');
    const ratingInput = document.getElementById('id_rating');
    
    if (starContainer && ratingInput) {
        const stars = starContainer.querySelectorAll('.star');
        let currentRating = parseInt(ratingInput.value) || 0;
        
        if (currentRating > 0) {
            updateStarsState(currentRating, 'active');
        }

        stars.forEach(star => {
            star.addEventListener('mouseover', function() {
                const val = parseInt(this.getAttribute('data-value'));
                updateStarsState(val, 'hover');
            });
            
            star.addEventListener('mouseout', function() {
                stars.forEach(s => s.classList.remove('hover'));
            });
            
            star.addEventListener('click', function() {
                currentRating = parseInt(this.getAttribute('data-value'));
                ratingInput.value = currentRating;
                updateStarsState(currentRating, 'active');
            });
        });
        
        function updateStarsState(value, className) {
            if (className === 'active') {
                stars.forEach(s => s.classList.remove('active'));
            }
            stars.forEach(s => {
                const starVal = parseInt(s.getAttribute('data-value'));
                if (starVal <= value) {
                    s.classList.add(className);
                }
            });
        }
    }
});
