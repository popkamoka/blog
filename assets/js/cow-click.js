const image = document.getElementById("alienCowImage");
const sound = document.getElementById("cowSound");
const texte = document.getElementById("messageVache");
const transformSound = new Audio(baseUrl + "/audio/mort.ogg"); // Son de transformation

let clickCount = 0;
const ouchExpressions = [
  "ouille", // français
  "ouch", // anglais
  "ay", // espagnol
  "autsch", // allemand
  "ahi", // italien
  "ai", // portugais
  "au", // néerlandais
  "aj", // suédois
  "ай", // russe
  "itai", // japonais
  "哎呀", // chinois (mandarin)
  "아야", // coréen
  "آه", // arabe
];

if (image && sound) {
  image.addEventListener("click", function () {
    // Si une animation est en cours, on ne fait rien
    if (image.classList.contains("is-animating")) {
      return;
    }

    // Ajoute l'animation de pulsation et de couleur rouge (dommages)
    image.classList.add("cow-clicked");
    // Empêche le clic pendant l'animation
    image.classList.add("is-animating");

    // Supprime la classe après l'animation
    setTimeout(function () {
      image.classList.remove("cow-clicked");
      // Restaure les événements de clic après l'animation
      image.classList.remove("is-animating");
    }, 300); // Durée de l'animation de pulsation (300ms)

    clickCount++;

    // Si moins de 10 clics, jouer le son habituel
    if (clickCount < 10) {
      const randomMessage =
        ouchExpressions[Math.floor(Math.random() * ouchExpressions.length)];
      texte.textContent = randomMessage;

      sound.load();
      sound.play();
    }

    // Après 10 clics, transformer l'image en steak et ajouter une nouvelle animation
    if (clickCount === 10) {
      texte.textContent = "sale batard je suis mort";

      // Ajouter l'animation steak (rétrécissement de la vache)
      image.classList.add("steak-appearance");

      // Jouer un son de transformation (ou autre effet sonore)
      transformSound.play();

      // Attendre la fin de l'animation de transformation de la vache
      setTimeout(function () {
        // Remplacer l'image de la vache par celle du steak
        image.src = baseUrl + "/images/beef.gif"; // Remplacer la vache par le steak
        // Retirer l'animation de rétrécissement de la vache
        image.classList.remove("steak-appearance");

        // Ajouter l'animation d'apparition du steak
        image.classList.add("steak-reveal");
      }, 600); // Attendre la fin de l'animation de rétrécissement (600ms)

      // Désactiver l'écouteur de clic après la transformation
      image.removeEventListener("click", arguments.callee);

      // Désactiver les clics supplémentaires
      image.style.pointerEvents = "none"; // Rendre l'image non-cliquable après la transformation
    }
  });
}
