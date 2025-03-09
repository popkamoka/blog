const image = document.getElementById("alienCowImage");
const sound = document.getElementById("cowSound");

if (image && sound) {
  image.addEventListener("click", function () {
    sound.load();
    sound.play();
  });
}
