document.addEventListener('DOMContentLoaded', () => {
    console.log("Gravity Fitness JS Loaded");
    // Basic carousel auto-scroll (optional)
    const carousel = document.querySelector('.carousel-inner');
    if (carousel) {
        let scrollPosition = 0;
        setInterval(() => {
            scrollPosition += carousel.offsetWidth / 3;
            if (scrollPosition >= carousel.scrollWidth - carousel.offsetWidth) {
                scrollPosition = 0;
            }
            carousel.scrollTo({ left: scrollPosition, behavior: 'smooth' });
        }, 5000);
    }
});