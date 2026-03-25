document.addEventListener('DOMContentLoaded', () => {
    const introContainer = document.getElementById('intro-container');
    const mainContent = document.getElementById('main-content');

    // The Netflix CSS animation takes about 5 - 5.5s total to finish.
    setTimeout(() => {
        // Start fading out the intro
        introContainer.style.opacity = '0';

        // Wait for the fade out transition (1s as defined in CSS) to complete before hiding it completely
        setTimeout(() => {
            introContainer.classList.add('hidden');
            mainContent.classList.remove('hidden');

            // Small semantic animation for the main content entry
            mainContent.style.opacity = '0';
            mainContent.style.transition = 'opacity 1s ease-in';
            // Force reflow
            void mainContent.offsetWidth;
            mainContent.style.opacity = '1';
        }, 1000);

    }, 5300); // Wait 5.5 seconds for the N animation to fully play out
});
