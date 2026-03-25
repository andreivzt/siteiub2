// Configurare pagini
const totalPages = 7;
let currentPage = 1;

// Functie pentru intoarcerea paginii inainte (click pe dreapta)
function turnPage(leafIdNum) {
    if (leafIdNum > totalPages) return;

    // Gasim foaia care trebuie intoarsa
    const leafToTurn = document.getElementById(`leaf${leafIdNum}`);

    // Adaugam clasa de flip
    leafToTurn.classList.add('flipped');

    // Adjustam z-index-ul pentru ca pagina viitoare sa fie deasupra pe stanga
    setTimeout(() => {
        leafToTurn.style.zIndex = 10 + leafIdNum;

        // Centram cartea deschisa pe ecran
        if (leafIdNum === 1) {
            if (window.innerWidth > 900) {
                document.querySelector('.book-container').style.transform = 'translateX(0)';
            }
        }
    }, 400); // Jumătatea animației

    currentPage = leafIdNum + 1;
}

// Functie pentru intoarcerea paginii inapoi (click pe stanga)
function turnBack(leafIdToReturn) {
    // Foaia pe care vrem să o aducem înapoi
    const leafToTurnBack = document.getElementById(`leaf${leafIdToReturn}`); // ex: cand sunt pe 2, ma intorc pe 1

    leafToTurnBack.style.zIndex = 10 + leafIdToReturn + 5; // Ii dam un z-index mai temporar la intoarcere

    // Scoatem clasa de flip
    leafToTurnBack.classList.remove('flipped');

    setTimeout(() => {
        leafToTurnBack.style.zIndex = totalPages - leafIdToReturn + 1; // Restauram z-index-ul corect pentru partea dreapta

        if (leafIdToReturn === 1) {
            // Inchidem cartea, o centram iar ca o carte inchisa
            if (window.innerWidth > 900) {
                document.querySelector('.book-container').style.transform = 'translateX(-25%)';
            }
        }
    }, 400);

    currentPage = leafIdToReturn;
}

// --- Logica pentru surpriza ---

const magicBtn = document.getElementById('magic-btn');
const surpriseOverlay = document.getElementById('surprise-overlay');
const closeSurprise = document.getElementById('close-surprise');
const heartsContainer = document.getElementById('hearts-container');
let isFallingInterval;

// Deschidere surpriza
magicBtn.addEventListener('click', () => {
    surpriseOverlay.classList.remove('hidden');
    startFallingHearts();
});

// Inchidere surpriza
closeSurprise.addEventListener('click', () => {
    surpriseOverlay.classList.add('hidden');
    stopFallingHearts();
});

// Creare inimioare cazatoare
function createHeart() {
    const heart = document.createElement('div');
    heart.classList.add('falling-heart');

    // Emojis array (inimioare si alte ilustratii romantice)
    const hearts = ['❤️', '💖', '💕', '🌹', '✨', '🥰'];
    heart.innerText = hearts[Math.floor(Math.random() * hearts.length)];

    // Pozitie random orizontala
    heart.style.left = Math.random() * 100 + 'vw';

    // Durata animatie random
    const animationDuration = Math.random() * 3 + 4; // Intre 4s si 7s
    heart.style.animationDuration = animationDuration + 's';

    // Marime random
    heart.style.fontSize = (Math.random() * 1.5 + 1) + 'rem';

    heartsContainer.appendChild(heart);

    // Stergem inimioara dupa ce cade pentru a nu incarca DOM-ul
    setTimeout(() => {
        heart.remove();
    }, animationDuration * 1000);
}

function startFallingHearts() {
    // Curatam container-ul in caz ca a ramas ceva
    heartsContainer.innerHTML = '';

    // Generam inimioare mai des la inceput
    for (let i = 0; i < 15; i++) {
        setTimeout(createHeart, Math.random() * 2000);
    }

    // Continuam sa generam inimioare
    isFallingInterval = setInterval(createHeart, 300);
}

function stopFallingHearts() {
    clearInterval(isFallingInterval);
}

// Initializare
// nu mai este nevoie de transformari JS pt initializare din pricina arhitecturii de foi (leaves)

// Functie pentru butonul de "De la inceput"
function resetBook() {
    // Punem inapoi toate paginile
    for (let i = totalPages; i >= 1; i--) {
        const leaf = document.getElementById(`leaf${i}`);
        if (leaf.classList.contains('flipped')) {
            leaf.classList.remove('flipped');
            // Restauram logica de z-index
            leaf.style.zIndex = totalPages - i + 1;
        }
    }

    // Inchidem cartea, o centram iar ca o carte inchisa
    if (window.innerWidth > 900) {
        document.querySelector('.book-container').style.transform = 'translateX(-25%)';
    }

    currentPage = 1;
}
